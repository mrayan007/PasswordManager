import json
import questionary
from cryptography.fernet import Fernet

def Menu(message, menu) :
    return questionary.select(
        message, choices = menu
        ).ask()

def LoadAccounts() :
    try :
        with open("../Secrets/accounts.json", "r") as file :
            content = json.load(file)

        if content == []:
            return 0

        return content
        
    except FileNotFoundError:
        return 0
    
def LoadKey() :
    try :
        with open('../Secrets/secret.key', 'rb') as file :
            return file.read()
    except :
        key = Fernet.generate_key()

        with open ('../Secrets/secret.key', 'wb') as file :
            file.write(key)

        return key
    
def Encrypt(password) -> str :
    key = LoadKey()
    f = Fernet(key)

    return f.encrypt(password.encode()).decode()

def Decrypt(password) -> str :
    key = LoadKey()
    f = Fernet(key)

    return f.decrypt(password.encode()).decode()