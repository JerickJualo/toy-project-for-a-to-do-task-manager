from datetime import datetime 
from tasks import Task

#CLASS FOR ACCOUNT
class Account:
    
    # Class Attributes
    LIST_ACC_ID: list[int] = []
    ALL_ACC: list[str] = []
    NO_ACCOUNTS: int = 0
    DETAILS_ACCOUNT = {}
        
    
    def __init__(self, username: str, password: str):

        # Username, Password, Account ID
        key = username.lower()
        self.username = username
        self.password = password
        
        next_id: int = Account.LIST_ACC_ID[-1] + 1 if Account.LIST_ACC_ID else 1

        self.acc_id: int = next_id # Owner ID on Task Class
        
        #Task related
        
        self.tasks = {}
        

        #Actions to be executed for Class Attributes
        Account.LIST_ACC_ID.append(next_id)
        Account.ALL_ACC.append(self)
        Account.NO_ACCOUNTS += 1
        Account.DETAILS_ACCOUNT[key] = password 
        


    # Instance Methods

    #Account Details Display Methods

    def display_NO_ACCOUNTS(self) -> str:
        return f"Total Number of Accounts: {Account.NO_ACCOUNTS}"
    
    
    def display_accounts(self) -> str:
        return f"Account Details: {Account.DETAILS_ACCOUNT}"

    def view_acc_id(self) -> str:
        return f"Account: {self.username} ID: {self.acc_id}"
        
    def __repr__(self) -> str:
        return f"Account(Username: '{self.username}',Password: '{self.password}', Account ID: '{self.acc_id}')"
    
    # Task Related Methods

    def view_tasks(self):
        """
        1. Display all tasks for the account.
        2. If no tasks exist, inform the user.
        3. If tasks exist, display each task's details.
        """
        
        if not self.tasks:
            print("No tasks available for this account.")
            return
        
        print(f"Tasks for Account '{self.username}':")
        for task_id, task in self.tasks.items():
            print(f"Task ID: {task_id}, Name: {task.task_name}, Status: {task.status}, Date Created: {task.date_created.strftime('%Y-%m-%d %H:%M:%S')}")

        
        
    def create_task(self):
        print("Creating a new task:" )

        # a dictionary for task status options
        status = {"1": "Not Started",
            "2": "In Progress",
            "3": "Completed",
            "4": "On Hold"
        }

        # Asking the task detials

        task_name: str = input("Enter the task name: ")
        description: str = input("Enter the task description: ")
        status_choice: str = input("""Enter the task status: 
                                (1: Not Started 
                                2: In Progress
                                3: Completed
                                4: On Hold)
                                : """)
        
        # Validate the status choice and set the task status
        if status_choice in status:
            task_status = status[status_choice]
        else:
            print("Invalid status choice. Defaulting to 'Not Started'.")
            task_status = status["1"]

        #Instantiate a new Task object

        new_task = Task(task_name, description, task_status, self.acc_id)
        
        self.tasks[new_task.task_id] = new_task

        print(f"""Task '{new_task.task_name}' created successfully with status '{new_task.status}'!
            Task_ID: {new_task.task_id}
            Description: {new_task.description}
            Date Created: {new_task.date_created.strftime('%Y-%m-%d %H:%M:%S')}
            Week Day Created: {new_task.date_created.strftime("%A")}""")
            
        new_task.day_created = new_task.date_created.strftime("%A")
        
        return new_task

    

    
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







