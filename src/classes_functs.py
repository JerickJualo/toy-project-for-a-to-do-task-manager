from datetime import datetime 

#CLASS FOR ACCOUNT
class Account:
    
    list_acc_id = []
    all_acc = []
    no_accounts = 0
    details_account = {}
        
    
    
    def __init__(self, username: str, password: str):
        key = username.lower()
        self.username = username
        self.password = password
        
        next_id = Account.list_acc_id[-1] + 1 if Account.list_acc_id else 1
        self.acc_id = next_id
        Account.list_acc_id.append(next_id)
        Account.all_acc.append(self)
        
        Account.no_accounts += 1
        Account.details_account[key] = password 

    def display_no_accounts(self):
        return f"Total Number of Accounts: {Account.no_accounts}"
    
    
    def display_accounts(self):
        return f"Account Details: {Account.details_account}"

    def view_acc_id(self):
        return f"Account: {self.username} ID: {self.acc_id}"
        
    def __repr__(self):
        return f"Account(Username: '{self.username}',Password: '{self.password}', Account ID: '{self.acc_id}')"
    
    @staticmethod
    def create_account():

        """
    1. Loop until unique username + matching passwords
    2. Instantiate new account(...)
    3. Confirm creation, return to login flow
    """

        while True:
            
            print("Creating Account:")

            create_user: str  = input("Enter the Username: ")
    
            # Check if the username already exists
            if create_user in Account.details_account:
                print("Username already exists. Please try a different username.")
                continue
            
            first_password: str  = input("Enter the Password: ")
            final_password: str  = input("Confirm the Password: ")
            
            if first_password != final_password:
                print("Passwords do not match. Please try again.")
                continue
    
            
            new_account = Account(create_user, final_password)
            print(f"Account created successfully for {create_user}!")
            return new_account
            break
        
    
 # CLASS FOR TASKS   

    


#FUNCTION SECTIONS


def log_in():

    """
    1. Prompt for username/password
    2. Check against account.details_account
    3. On success: greet & return True
    4. On failure: call create_account() or exit
    """
    
    print("=======================================================================================================================================================")
    print("Log In:")
    username: str = input("\nEnter your username: ").lower()
    password: str = input("Enter your password: ")
    
    

    if username.lower() in Account.details_account and Account.details_account[username.lower()] == password:
        print(f"\nWelcome back, {username.title()}!")
        return True
        

    else:
        print("User is not found.")
        confirm: str  = input("\nDo you want to create an account? (y/n): ").lower()
        if confirm == "y":
            Account.create_account()
        else:
            print("Exiting the program. Please run again with the correct username.")
            exit()







