from datetime import datetime 

#CLASS FOR ACCOUNT
class Account:
    
    # Class Attributes
    LIST_ACC_ID: list[int] = []
    ALL_ACC: list[str] = []
    NO_ACCOUNTS: int = 0
    DETAILS_ACCOUNT: dict; {str: str} = {}
        
    
    def __init__(self, username: str, password: str):

        # Username, Password, Account ID
        key = username.lower()
        self.username = username
        self.password = password
        
        next_id: int = Account.LIST_ACC_ID[-1] + 1 if Account.LIST_ACC_ID else 1

        self.acc_id: int = next_id

        #Actions to be executed for Class Attributes
        Account.LIST_ACC_ID.append(next_id)
        Account.ALL_ACC.append(self)
        Account.NO_ACCOUNTS += 1
        Account.DETAILS_ACCOUNT[key] = password 
        


    # Instance Methods
    def display_NO_ACCOUNTS(self) -> str:
        return f"Total Number of Accounts: {Account.NO_ACCOUNTS}"
    
    
    def display_accounts(self) -> str:
        return f"Account Details: {Account.DETAILS_ACCOUNT}"

    def view_acc_id(self) -> str:
        return f"Account: {self.username} ID: {self.acc_id}"
        
    def __repr__(self) -> str:
        return f"Account(Username: '{self.username}',Password: '{self.password}', Account ID: '{self.acc_id}')"
    

    
    #Class Methods

    @classmethod
    def create_account(cls):

        """
    1. Loop until unique username + matching passwords
    2. Instantiate new account(...)
    3. Confirm creation, return to login flow
    """

        while True:
            
            print("Creating Account:")

            create_user: str  = input("Enter the Username: ")
    
            # Check if the username already exists
            if create_user in Account.DETAILS_ACCOUNT:
                print("Username already exists. Please try a different username.")
                continue
            
            first_password: str  = input("Enter the Password: ")
            final_password: str  = input("Confirm the Password: ")
            
            if first_password != final_password:
                print("Passwords do not match. Please try again.")
                continue
    
            print(f"Account created successfully for {create_user}!")
            return cls(create_user, final_password)
            break
 # CLASS FOR TASKS

    


#FUNCTION SECTIONS


def log_in():

    """
    1. Prompt for username/password
    2. Check against account.DETAILS_ACCOUNT
    3. On success: greet & return True
    4. On failure: call create_account() or exit
    """
    
    print("=======================================================================================================================================================")
    print("Log In:")
    username: str = input("\nEnter your username: ").lower()
    password: str = input("Enter your password: ")
    
    

    if username.lower() in Account.DETAILS_ACCOUNT and Account.DETAILS_ACCOUNT[username.lower()] == password:
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







