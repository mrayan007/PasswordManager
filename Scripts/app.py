import json
import utilities
from getpass import getpass
from pprint import pprint

def ShowAccounts() :
    accounts = utilities.LoadAccounts()

    if accounts == 0 :
        print('\nNo accounts to load.')
        return
    
    websitesMenuChoices = []

    for account in accounts :
        if account["website"] in websitesMenuChoices :
            continue

        websitesMenuChoices.append(account["website"])
    
    websiteChoice = utilities.Menu("\nSelect a website:", websitesMenuChoices)

    websiteChoiceAccounts = []
    websiteChoiceUsernames = []

    for account in accounts :
        if account["website"] == websiteChoice :
            websiteChoiceAccounts.append(account)
            websiteChoiceUsernames.append(account["username"])

    usernameChoice = utilities.Menu("\nSelect a username:", websiteChoiceUsernames)

    for account in websiteChoiceAccounts :
        if account["username"] == usernameChoice :
            user = account["username"]
            password = account["password"]
            break
    
    print(f"\nThe password for '{user}' is: {utilities.Decrypt(password)}")

def AddAccount() :
    accounts = utilities.LoadAccounts()

    if accounts == 0:
        accounts = []

    account = {}

    account['website']  = input  ("\nEnter website:")
    account['username'] = input  ("\nEnter username:")
    
    while True:
        password = getpass('\nEnter password:')
        passwordConfirmation = getpass('\nConfirm password:')

        if password == passwordConfirmation:
            break

        print('\nPasswords not matching, reconfirm.')

    account["password"] = utilities.Encrypt(password)

    print("\nYou entered:")
    pprint(account)

    accounts.append(account)

    with open("../Secrets/accounts.json", "w") as file :
        json.dump(accounts, file, indent = 4)

    print("\nAccount added successfully!\n")

def DeleteAccount() :
    accounts = utilities.LoadAccounts()

    if accounts == 0:
        print('\nYou have no accounts to delete!')
        return

    websitesMenu = []

    for account in accounts:
        websitesMenu.append(account['website'])

    websitesMenuChoice = utilities.Menu('\nSelect the website of your desired account:', websitesMenu)

    usernamesMenu = []

    for account in accounts:
        if account['website'] == websitesMenuChoice:
            usernamesMenu.append(account['username'])

    usernameToDelete = utilities.Menu('\nSelect the account to delete:', usernamesMenu)

    accountsAfterDeletion = []

    for account in accounts:
        if account['username'] == usernameToDelete:
            continue

        accountsAfterDeletion.append(account)

    with open('../Secrets/accounts.json', 'w') as file:
        json.dump(accountsAfterDeletion, file)

    print('\nAccount deleted successfully')