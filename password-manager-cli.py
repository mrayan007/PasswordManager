# libraries

# cryptography is a library that allows string encryption and decryption (needed when storing passwords)


# questionary is a library that allows me to create a cli with highlighted and selectable choices
import questionary

# allows writing files in json
import json

# getpass is a library that allows passwords to be hidden during input


# utilities

# helper function to make json.dumps() faster
def ToJson(dictionary) :
    return json.dumps(dictionary, indent = 4)

# method to load the fernet secret key from the secret.key file


# method to encrypt passwords


# method to decrypt stored passwords


# function to make a menu


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

# function to update account info
# def Update() :
#     try :
#         with open ('accounts.json', 'r') as file :
#             accounts = json.load(file)
#             if accounts == [] :
#                 print("\nYou have no accounts to update.\n")
#                 return
#     except :
#         print('\nNo accounts found to be updated.\n')
#         return

# function that executes main menu




# running app
print("\nWelcome to your local password safe!\n")
Main()