# libraries

# cryptography is a library that allows string encryption and decryption (needed when storing passwords)
from cryptography.fernet import Fernet

# questionary is a library that allows me to create a cli with highlighted and selectable choices
import questionary

# allows writing files in json
import json

# getpass is a library that allows passwords to be hidden during input
from getpass import getpass

# utilities

# helper function to make json.dumps() faster
def ToJson(dictionary) :
    return json.dumps(dictionary, indent = 4)

# method to load the fernet secret key from the secret.key file
def LoadKey() :
    try :
        with open('secret.key', 'rb') as file :
            return file.read()
    except :
        key = Fernet.generate_key()

        with open ('secret.key', 'wb') as file :
            file.write(key)

        return key

# method to encrypt passwords
def Encrypt(password) -> str :
    key = LoadKey()
    f = Fernet(key)

    return f.encrypt(password.encode()).decode()

# method to decrypt stored passwords
def Decrypt(password) -> str :
    key = LoadKey()
    f = Fernet(key)

    return f.decrypt(password.encode()).decode()

# function to make a menu
def Menu(message, menu) :
    return questionary.select(
        message, choices = menu
        ).ask()

# main functions

# method for adding a new account
def Add() :
    try:
        with open("accounts.json", "r") as file :
            accounts = json.load(file)
    except :
        accounts = []

    account = {}

    account['website']  = input("Enter website:        ")
    account['username'] = input("Enter username:       ")
    password            = getpass("Enter password:     ")
    confirmPass         = getpass("Confirm your password:")

    while password != confirmPass :
        print("\nYour passwords don't match, try again!\n")

        password = getpass("Enter password:        ")
        confirmPass = getpass("Confirm your password:")

    account["password"] = Encrypt(password)

    # with json.dumps() you can structure dictionary data nicely
    print(f"\nYou entered:\n{ToJson(account)}\n")

    accounts.append(account)

    with open("accounts.json", "w") as file :
        # used indent = 4 for better json readability
        json.dump(accounts, file, indent = 4)

    print("\nAccount added successfully!\n")

# function to show usernames and passwords
def Show() :
    try :
        with open("accounts.json", "r") as file :
            accounts = json.load(file)
    except :
        print("\nYou have no accounts saved yet.\n")
        return
    
    websiteMenu = []

    for account in accounts :
        # to avoid duplication of the same website in menu
        if account["website"] in websiteMenu :
            continue

        websiteMenu.append(account["website"])
    
    chosenWebsite = Menu("\nSelect a website: \n", websiteMenu)

    websiteAccounts = []
    usernameMenu = []

    for account in accounts :
        if account["website"] == chosenWebsite :
            websiteAccounts.append(account)
            usernameMenu.append(account["username"])

    chosenUser = Menu("\nSelect a username:\n", usernameMenu)

    for account in websiteAccounts :
        if account["username"] == chosenUser :
            user = account["username"]
            password = account["password"]
            break
    
    print(f"\nThe password for {user} is: {Decrypt(password)}\n")

# function to delete accounts
def Delete() :
    try :
        with open("accounts.json", "r") as file :
            accounts = json.load(file)

            if accounts == [] :
                print("\nYou have no accounts to delete.\n")
                return
    except : 
        print("\nYou have no accounts to delete.\n")
        return
    
    deleteMenu = [
        "Delete All",
        "Delete an Account",
        "\nBack\n"
    ]

    option = Menu("\nChoose an option:\n", deleteMenu)

    if option == "Delete All" :
        newAccounts = []
        print("\nAccounts deleted successfully!\n")
    elif option == "Delete an Account" :
        websiteMenu = []

        for account in accounts :
            if account["website"] in websiteMenu :
                continue

            websiteMenu.append(account["website"])
        
        chosenWebsite = Menu("\nSelect a website: \n", websiteMenu)

        usernameMenu = []

        for account in accounts :
            if account["website"] == chosenWebsite :
                usernameMenu.append(account["username"])

        chosenUser = Menu("\nSelect a username:\n", usernameMenu)

        newAccounts = []

        for account in accounts :
            if account["username"] == chosenUser :
                continue
        
            newAccounts.append(account)

        print("\nAccount deleted successfully!\n")
    else :
        return

    with open("accounts.json", "w") as file :
        json.dump(newAccounts, file)

# function to start app
def Start() :
    while True :
        # the choices to show in the menu
        menuChoices = [
            "Show Accounts",
            "Add Account",
            "Delete Account",
            "Quit"
        ]

        menuChoice = Menu("Select an option:", menuChoices)

        # map index of menu choice to variable to make if statement later shorter
        choiceIndex = menuChoices.index(menuChoice)

        if (choiceIndex == 0) :
            print("\nLoading accounts...\n")
            Show()
        elif (choiceIndex == 1) :
            Add()
        elif choiceIndex == 2 :
            Delete()
        else :
            print("\nLogging out...\n")
            break

# running app
print("\nWelcome to your local safe!\n")
Start()