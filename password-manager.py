# questionary is a library that allows me to create a cli with highlighted and selectable choices
import questionary

import json

# getpass is a library that allows passwords to be hidden during input
from getpass import getpass

quit = False

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

def Show() :
    try :
        with open("accounts.json", "r") as file :
            accounts = json.load(file)
    except :
        accounts = [{"Error": "No accounts saved yet."}]
    
    print(f"\nYour accounts:\n{ToJson(accounts)}\n")

# function to make a menu
def Menu(message, choices) :
    return questionary.select(
        message, choices = choices
        ).ask()

def Main() :
    global quit

    print("\nWelcome to your local safe!\n")

    # the choices to show in the menu
    menuChoices = [
        "Show Passwords",
        "Add Password",
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
    else :
        print("\nLogging out...\n")
        quit = True

class Program :
    while not quit :
        Main()