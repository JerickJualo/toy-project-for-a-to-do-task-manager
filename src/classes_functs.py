class account:
    no_accounts = 0
    details_account = {"jerick": "jualo"}
    
    
    def __init__(self, username: str, password: str):
        key = username.lower()
        self.username = username
        self.password = password
        account.no_accounts += 1
        account.details_account[key] = password

    def display_no_accounts(self):
        return f"Total Number of Accounts: {account.no_accounts}"
    
    
    def display_accounts(self):
        return f"Account Details: {account.details_account}"
    

def log_in():
    print("=======================================================================================================================================================")
    print("Log In:")
    username: str = input("\nEnter your username: ").lower()
    password: str = input("Enter your password: ")
    

    if username.lower() in account.details_account:
        print(f"\nWelcome back, {username.title()}!")
        return True
        

    else:
        print("User is not found.")
        confirm: str  = input("\nDo you want to create an account? (y/n): ").lower()
        if confirm == "y":
            create_account()
        else:
            print("Exiting the program. Please run again with the correct username.")
            exit()



def create_account():
    while True:
        
        print("Creating Account:")

        create_user: str  = input("Enter the Username: ")

        # Check if the username already exists
        if create_user in account.details_account:
            print("Username already exists. Please try a different username.")
            continue
        
        first_password: str  = input("Enter the Password: ")
        final_password: str  = input("Confirm the Password: ")
        
        if first_password != final_password:
            print("Passwords do not match. Please try again.")
            continue

        
        new_account = account(create_user, final_password)
        print(f"Account created successfully for {create_user}!")
        break
    

    
  