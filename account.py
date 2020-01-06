import json

from security import generate_id

ACCOUNT_FNAME = "data/accounts_data.json"

AVAILABLE = 'available'
ARCHIVED = 'archived'
ALL_STATUS = (AVAILABLE, ARCHIVED)

MODE_PRIVATE = 'private'
MODE_COMPANY = 'company'
ALL_MODES = (MODE_PRIVATE, MODE_COMPANY)

DEFAULT_BALANCE = 100


class AccountManager:
    def __init__(self, source=ACCOUNT_FNAME):
        self.source = source
        with open(self.source, 'r') as f:
            try:
                self._data = json.load(f)
            except ValueError:
                self._data = {}

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, account):
        self._data.update(account)

    def save_file(self):
        with open(self.source, 'w') as f:
            json.dump(self._data, f)

    # file -> dict
    def get_account(self, client, account_id) -> dict:
        try:
            account_data = self.data[client]
        except KeyError:
            print(f"There is no accounts connected with {client}")
            return {}

        for account in account_data:
            if account['account_id'] == account_id:
                return account

        print(f"Account '{account_id} not found.")
        return {}

    # dict -> file
    # Account -> dict -> file
    def save_account(self, client, account):
        account_data = {
            "account_id": account.account_id,
            "mode": account.mode,
            "status": account.status,
            "balance": account.balance
        }
        self.data[client].append(account)

    def ensure_client_existence(self, client) -> bool:
        if client not in self.data.keys():
            print(f"There is no client data named {client}. Created empty set.")
            self.data.update({client: []})

        return True

    def limit_company_accounts(self, client):
        cnt = 0
        for account in self.data[client]:
            if account['mode'] == MODE_COMPANY:
                cnt += 1

        return True if cnt > 1 else False

    def archive(self, client, index):
        self.data[client][index]['status'] = ARCHIVED

    def dearchive(self, client, index):
        self.data[client][index]['status'] = AVAILABLE


class Account:
    def __init__(self, owner, AM):
        self.AM = AM
        self.owner = owner
        self.account_id = generate_id()
        self.mode = self.set_mode()
        self.status = AVAILABLE
        self.balance = DEFAULT_BALANCE

    def set_mode(self) -> str:
        mode = input("What kind of account should it be? (private/company) ")
        if mode not in ALL_MODES:
            mode = MODE_PRIVATE
            print("Wrong account mode!\nSet to private as default.")

        if mode == MODE_COMPANY and self.AM.limit_company_accounts(self.owner):
            print("You already got rid of company accounts slot!"
                  "\nSetting the new account's mode to private.")
            mode = MODE_PRIVATE

        return mode

    def withdrawal(self, value):
        self.balance -= value

    def remittance(self, value):
        self.balance += value
