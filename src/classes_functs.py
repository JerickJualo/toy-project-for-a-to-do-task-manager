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
    
    
    def full_acc_details(self) -> str:
        print("==========================")
        print(f"Account Details for {self.username}:")
        print(f"Username: {self.username}")
        print(f"Account ID: {self.acc_id}")
        print("========================================================================================================================================================")

        for x in self.tasks.values():
            print(x)
        print("========================================================================================================================================================")
        return ""

        
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
        print("========================================================================================================================================================")
        print(f"Tasks for Account '{self.username}':")
        print("========================================================================================================================================================")
        for task_id, task in self.tasks.items():
            print(f"Task ID: {task_id}, Name: {task.task_name}, Status: {task.status}, Date Created: {task.date_created.strftime('%Y-%m-%d %H:%M:%S')} , Due Date: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'No due date set'}")

        print("========================================================================================================================================================")

    def create_task(self):
        print("\n========================================================================================================================================================")
        print("Creating a new task:\n" )

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
            print("========================================================================================================================================================")
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

    def delete_task(self, task_id: int):
        """
        1. Check if the task exists in the account's tasks.
        2. If it exists, delete the task and inform the user.
        3. If it doesn't exist, inform the user.
        """
        
        if task_id in self.tasks:
            confirm = input("Do you really want to delete this task? (yes/no): ").strip().lower()

            if confirm == "yes":
                task = self.tasks.pop(task_id)

                if task in Task.ALL_TASKS:
                    Task.ALL_TASKS.remove(task)
                if task_id in Task.LIST_TASK_ID:
                    Task.LIST_TASK_ID.remove(task_id)
                Task.NO_TASKS -= 1

                if Task.NO_TASKS > 0:
                    Task.NO_TASKS -= 1
                
                print(f"Task with ID {task_id} has been deleted.")

                return True
            
            else:
                print("Task deletion cancelled.")
        else:
            print(f"Task with ID {task_id} does not exist in this account.")

    
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

    def to_dict(self) -> dict:
        return {
            "acc_id":   self.acc_id,
            "username": self.username,
            "password": self.password,
            "task_ids": list(self.tasks.keys()),
        }

    @classmethod
    def from_dict(cls, data: dict):
        # 1) Create a bare instance without calling __init__
        acct = cls.__new__(cls)

        # 2) Manually set instance attributes
        acct.username = data["username"]
        acct.password = data["password"]
        acct.acc_id   = data["acc_id"]
        acct.tasks    = {}           # start empty; load_data() will fill this in

        # 3) Update class‑level registries exactly once
        Account.LIST_ACC_ID.append(acct.acc_id)
        Account.ALL_ACC.append(acct)
        Account.NO_ACCOUNTS += 1
        Account.DETAILS_ACCOUNT[acct.username.lower()] = acct.password

        return acct


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
    log_username: str = input("\nEnter your username: ").lower()
    log_password: str = input("Enter your password: ")
    print("=======================================================================================================================================================")
    
    

    if log_username.lower() in Account.DETAILS_ACCOUNT and Account.DETAILS_ACCOUNT[log_username.lower()] == log_password:
        for acc in Account.ALL_ACC:
            if acc.username == log_username:
                global logged_acc
                logged_acc = acc
                break

        return logged_acc

    else:
        print("User is not found.")
        confirm: str  = input("\nDo you want to create an account? (y/n): ").lower()
        if confirm == "y":
            Account.create_account()
        else:
            print("Exiting the program. Please run again with the correct username.")
            exit()







