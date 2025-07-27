import argon2
from argon2.exceptions import VerifyMismatchError
import utilities
import app

hasher = argon2.PasswordHasher() 

def MainMenu() :
    mainMenuOptions = [
            "Show Accounts",
            "Add Account",
            "Delete Account",
            "Update Account",
            "Quit"
            ]

    while True :
        userMainMenuChoice = utilities.Menu("\nSelect an option:", mainMenuOptions)

        choiceIndex = mainMenuOptions.index(userMainMenuChoice)

        if (choiceIndex == 0) :
            print("\nLoading accounts...")
            app.ShowAccounts()
        elif (choiceIndex == 1) :
            app.AddAccount()
        elif choiceIndex == 2 :
            Delete()
        else :
            print("\nLogging out...\n")
            break

def Main():
    print('\nWelcome to your safehouse!')

    try:
        with open('../Secrets/master.key', 'r') as file:
            masterKeyHash = file.read()

        entryTries = 4

        while True:
            keyInput = input('\nEnter your key:')

            try:
                hasher.verify(masterKeyHash, keyInput)
                break
            except VerifyMismatchError:
                entryTries -= 1

                if entryTries == 0 :
                    print('\nNo tries left, exiting application...')
                    return
                
                print(f'\n❌ Key is incorrect, {entryTries} tries left.')

    except FileNotFoundError:
        print('\n🔐 Create a master key — only with it can you access your vault!')
        masterKey = input('\nNote it down somewhere safe:')

        with open('../Secrets/master.key', 'w') as file:
            file.write(hasher.hash(masterKey))

    MainMenu()

Main()