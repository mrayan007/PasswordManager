# questionary is a library that allows me to create a cli with highlighted and selectable choices
import questionary

import json

quit = False

# helper function to make json.dumps() faster
def ToJson(dictionary) :
    return json.dumps(dictionary, indent = 4)

def Add() :
    try:
        with open("passwords.json", "r") as file :
            accounts = json.load(file)
    except :
        accounts = []

    account = {}

    account['website']  = input("Enter website:     ")
    account['username'] = input("Enter username:    ")
    account['password'] = input("Enter password:    ")

    # with json.dumps() you can structure dictionary data nicely
    print(f"You entered:\n{ToJson(account)}")

    accounts.append(account)

    with open("passwords.json", "w") as file :
        # used indent = 4 for better json readability
        json.dump(accounts, file, indent = 4)

    print("Account added successfully!")

def Show() :
    with open("passwords.json", "r") as file :
        accounts = json.load(file)
    
    print(f"Your accounts:\n{ToJson(accounts)}")

# the choices to show in the menu
menuChoices = [
    "Show Passwords",
    "Add Password",
    "Quit"
]

def Main() :
    global quit

    # this function shows all choices and returns the selected one
    menuChoice = questionary.select(
        "Select an option:", choices = menuChoices
    ).ask()

    # map index of menu choice to variable to make if statement later shorter
    choiceIndex = menuChoices.index(menuChoice)

    if (choiceIndex == 0) :
        print("Loading passwords...")
        Show()
    elif (choiceIndex == 1) :
        Add()
    else :
        quit = True

while not quit :
    Main()