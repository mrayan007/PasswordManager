# questionary is a library that allows me to create a cli with highlighted and selectable choices
import questionary

import json

# getpass is a library that allows passwords to be hidden during input
from getpass import getpass

# helper function to make json.dumps() faster
def ToJson(dictionary) :
    return json.dumps(dictionary, indent = 4)

def Add() :
    try:
        with open("accounts.json", "r") as file :
            accounts = json.load(file)
    except :
        accounts = []

    account = {}

    account['website']  = input("Enter website:     ")
    account['username'] = input("Enter username:    ")
    account['password'] = getpass("Enter password:    ")

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
        print("You have no accounts saved yet.")
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
    
    print(f"\nThe password for {user} is: {password}\n")

# function to delete accounts
def Delete() :
    try :
        with open("accounts.json", "r") as file :
            accounts = json.load(file)
    except : 
        print("You have no accounts to delete.")
        return
    
    deleteMenu = [
        "Delete All",
        "Delete an Account",
        "\nBack\n"
    ]

    option = Menu("\nChoose an option:\n", deleteMenu)

    if option == "Delete All" :
        newAccounts = []
        print("Accounts deleted successfully!")
    elif option == "Delete an Account" :
        websiteMenu = []

        for account in accounts :
            # to avoid duplication of the same website in menu
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

    else :
        Start()

    with open("accounts.json", "w") as file :
        json.dump(newAccounts, file)
    
    Start()
                

# function to make a menu
def Menu(message, menu) :
    return questionary.select(
        message, choices = menu
        ).ask()

def Start() :
    print("\nWelcome to your local safe!\n")

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

Start()