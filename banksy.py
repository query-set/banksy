#!/usr/bin/python3

from client import ClientManager, Client
from account import AccountManager, Account

LOGIN_CHOICES = ('l', 'c', 'x')
ACCOUNT_CHOICES = ('l', 'c', 'a', 'd', 'x')


def account_loop(client):
    AM = AccountManager()
    while True:
        print(f"\nCurrently logged user: {client.login}")
        choice = input("-- [L]ist accounts, "
                       "[C]reate new account, "
                       "[A]rchive or [D]earchive existing account, "
                       "Logout[x]: ")

        if choice.lower().strip() not in ACCOUNT_CHOICES:
            print(f"I do not recognize '{choice}' command.")

        elif choice.lower().strip() == ACCOUNT_CHOICES[0]:
            client.account_list()

        elif choice.lower().strip() == ACCOUNT_CHOICES[1]:
            ac = Account(client.login, AM)
            print(f"Successfully created new {ac.mode} with ID '{ac.account_id}'.")
            client.append_created_account(ac.account_id)
            if AM.ensure_client_existence(client.login):
                AM.save_account(client.login, ac)

        elif choice.lower().strip() == ACCOUNT_CHOICES[2]:
            client.account_list()
            w = int(input("Which of the following accounts you want to archive? ")) - 1
            AM.archive(client.login, w)

        elif choice.lower().strip() == ACCOUNT_CHOICES[3]:
            client.account_list()
            w = int(input("Which of the following accounts you want to dearchive? ")) - 1
            AM.dearchive(client, w)

        elif choice.lower().strip() == ACCOUNT_CHOICES[4]:
            print(f"\n'{client.login}' has log out\n")
            break

        AM.save_file()


def client_loop():
    print("-- Available commands:")

    CM = ClientManager()

    while True:
        choice = input(">> [L]ogin, [C]reate new Client account, e[x]it: ")

        if choice.lower().strip() not in LOGIN_CHOICES:
            print(f"I do not recognize {choice} command.")

        elif choice.lower().strip() == LOGIN_CHOICES[0]:
            print(CM.data)
            client = Client().sign_in(CM)
            if client:
                account_loop(client)
                CM.save_file()
            else:
                print("Cannot perform logging in.")

        elif choice.lower().strip() == LOGIN_CHOICES[1]:
            Client().create(CM)

        elif choice.lower().strip() == LOGIN_CHOICES[2]:
            print("\nSee you next time!")
            break


if __name__ == "__main__":
    client_loop()
