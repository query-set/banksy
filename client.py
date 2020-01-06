import getpass
import json

CLIENT_FNAME = "data/client_data.json"


class ClientManager:
    def __init__(self, source=CLIENT_FNAME):
        self.source = source
        with open(self.source, 'r') as f:
            try:
                self._data = json.load(f)
            except ValueError as e:
                print(e)
                self._data = {}

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, client):
        self._data.update(client)

    def save_file(self):
        with open(self.source, 'w') as f:
            json.dump(self.data, f)

    # file -> dict
    def get_client(self, login) -> dict:
        try:
            client = self.data[login]
        except KeyError:
            client = {}

        return client

    # dict -> file
    def save_client(self, client):
        client_data = {
            client.login: {
                "password": client.password,
                "list_of_accounts": client.loa
            }
        }
        self.data = client_data


class Client:
    def __init__(self):
        self.login = ''
        self.password = ''
        self.data = {}
        self.loa = []

    @classmethod
    def create(cls, CM):
        print("Creating new user...")
        cls.login = input("Login: ")
        if CM.get_client(cls.login):
            return "There is already a Client associated with that login!"
        elif not cls.login:
            return "You did not enter anything"

        cls.password = getpass.getpass()
        if not cls.password:
            return "Password must have non-zero length"

        cls.loa = []
        print("Successfully created a Client.")
        CM.save_client(cls)
        return cls

    def sign_in(self, CM):
        log = input("Login: ")
        self.data = CM.get_client(log)

        if not log or not self.data:
            print("Wrong login!")
            return None

        pas = getpass.getpass()
        if not pas or pas != self.data['password']:
            print("Wrong password!")
            return None

        print("Logged successfully!")
        self.login = log
        self.loa = self.data['list_of_accounts']

        return self

    def append_created_account(self, aid):
        self.loa.append(aid)

    def account_list(self):
        if not self.loa:
            print("\nThat client has no accounts.\nMay you want to create one?")

        for idx, acc in enumerate(self.loa):
            print(f"{idx + 1}. account '{acc}'")
