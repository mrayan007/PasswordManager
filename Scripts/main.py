import os
import argon2
from argon2.exceptions import VerifyMismatchError

hasher = argon2.PasswordHasher() 

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

Main()