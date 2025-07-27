import utilities

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