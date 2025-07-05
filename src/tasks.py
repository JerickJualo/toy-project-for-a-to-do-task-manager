from datetime import datetime

#CLASS SECTION

class Task:

    statuses: list = ["Not Started", "In Progress", "Completed", "On Hold"]

    #Task Class Attributes
    ALL_TASKS: list = []
    NO_TASKS: int = 0
    LIST_TASK_ID: list[int] = []

    def __init__(self, task_name: str, description: str, status: str = "Not Started", owner_id: int = None):

        # Owner ID 
        self.owner_id = owner_id

        #Task ID generation
        next_id: int = Task.LIST_TASK_ID[-1] + 1 if Task.LIST_TASK_ID else 1
        self.task_id: int = next_id

        # Task details attributes
        
        self.task_name = task_name
        self.description = description
        self.status = status
        self.details = {}

        #Task date attributes
        self.date_created = datetime.now()
        self.due_date = None
        self.day_created = None
        

        # Add the new task to the list of all tasks and update the task count
        Task.ALL_TASKS.append(self)
        Task.NO_TASKS += 1
        Task.LIST_TASK_ID.append(self.task_id)
        
    def __repr__(self) -> str:
        return f"Task(Task ID: '{self.task_id}', Owner ID: '{self.owner_id}', Task Name: '{self.task_name}', Description: '{self.description}', Status: {self.status})"
    
    def __str__(self) -> str:
        return f"""
        ===========================
        Task Information
        ===========================
        Task ID: {self.task_id}
        Owner ID: {self.owner_id}

        ===========================
        Task Details:
        ===========================
        Task Name: {self.task_name}
        Description: {self.description}
        Status: {self.status}
        Date Created: {self.date_created}
        Due Date: {self.due_date}
        Day Created: {self.day_created}
        """


    def set_due_date(self):
            
            """
            1. Set the due date for the task.
            2. The user will be prompted to enter the year,
               month, and day for the due date.
            3. The month will be selected from a list of months,
               and the day must be valid for the selected month.
            4. The due date will be stored as a datetime object.
            5. If the user enters an invalid date, they will be prompted to try again
            6. The due date will be displayed to the user.
            """

            # Dictionary to map month numbers to month names 
            month_list = {"1": "January", "2": "February", "3": "March", "4": "April", "5":"May", "6": "June",
                            "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
            
            # Dictionary to hold the maximum days in each month
            month_day_limit = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
                            "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
            
            while True:

                print(f"Set the Due date of the task {self.task_name}:")

                year: str = input("Enter the Year(eg. 2025): ").strip()

                if len(year) != 4 or not year.isdigit() and year > self.date_created.strftime("%Y"):
                    print("Invalid Year Format, Please Enter a valid year in YYYY format.")
                    continue
                else:
                    break

            while True:

                month_choice: str = input("""Enter the Number of the Month:
                            January - 1
                            February - 2
                            March   - 3
                            April   - 4
                            May     - 5
                            June    - 6
                            July    - 7
                            August  - 8
                            September - 9
                            October   - 10
                            November  - 11
                            December  - 12
                            : """).strip()
                
                
                
                if month_choice not in month_list:
                    print("Invalid Month Choice, Please try again. ")
                    continue
                
                month = month_list[month_choice]
                day_limit = month_day_limit[month]
                break
                    
            
            #Ensure the day not exceed the 31 day month limit
            while True:

                day = input("Enter the Day(eg. 1, 10, 25): ").strip()

                if int(day) > day_limit:
                    print(f"Invalid day, Please Enter a day within {month_day_limit[month]} days limit for {month}.")
                    continue

                break

            y = int(year)
            m = int(month_choice)
            d = int(day)
            
            self.due_date = datetime(y, m, d)
            print(f"{self.task_name} due date is now set!: {self.due_date}")

            return self.due_date
    




    def rename(self, new_task_name: str):
        """
        Change the name of the task.
        """

        if not new_task_name:
            print("Task name cannot be empty. Please provide a valid name.")
            return None

        confirmation = input(f"Are you sure you want to change the task name from {self.task_name} to {new_task_name}? (yes/no): ").strip().lower()

        if confirmation == "yes":

            self.task_name = new_task_name
            print(f"Task name changed to: {self.task_name}")
            return self.task_name
        
        else:
            print("Change Task Name Cancelled")
            return None
    



    
    def change_description(self, new_description: str):
        """
        Change the description of the task.
        """

        if not new_description:
            print("Description cannot be empty. Please provide a valid description.")
            return None
        
        confirmation = input(f"Are you sure you want to change the description of {self.task_name} to '{new_description}'? (yes/no): ").strip().lower()

        if confirmation == "yes":

            self.description = new_description
            print(f"Task description changed to: {self.description}")
            return self.description
        
        else:
            print("Change Description Cancelled")

            return None




    def change_status(self, new_status: str):

        """
        Change the status of the task.
        """

        if new_status not in Task.statuses:
            print(f"Invalid status. Please choose from: {', '.join(Task.statuses)}")
            return None
        
        confirmation = input(f"Are you sure you want to change the status of {self.task_name} to {new_status}? (yes/no): ").strip().lower()
        
        if confirmation == 'yes':
            self.status = new_status
            print(f"Status of {self.task_name} changed to: {self.status}")
            return self.status
        else:
            print("Status change cancelled.")
            return None
        
    def change_due_date(self):
        """
        Change the due date of the task.
        """

        new_due_date = self.set_due_date()
        
        confirmation = input(f"Are you sure you want to change the due date of {self.task_name} to {self.due_date}? (yes/no): ").strip().lower()

        if confirmation == "yes":
            self.due_date = new_due_date
            print(f"Due date changed to: {self.due_date}")
            return self.due_date
        
        else:
            print("Change Due Date Cancelled")
            return None
        
    # METHODS FOR SERIALIZATION
    
    def to_dict(self) -> dict:
        return {
            "task_id":      self.task_id,
            "owner_id":     self.owner_id,
            "task_name":    self.task_name,
            "description":  self.description,
            "status":       self.status,
            "date_created": self.date_created.isoformat(),
            "due_date":     self.due_date.isoformat() if self.due_date else None,
            "day_created":  self.day_created,
        }

    @classmethod
    def from_dict(cls, data: dict):
        
        task = cls(
            data["task_name"],
            data["description"],
            data["status"],
            data["owner_id"],
        )
       
        task.task_id      = data["task_id"]
        task.date_created = datetime.fromisoformat(data["date_created"])
        task.due_date     = datetime.fromisoformat(data["due_date"]) if data["due_date"] else None
        task.day_created  = data["day_created"]
        

        Task.LIST_TASK_ID.append(task.task_id)
        Task.ALL_TASKS.append(task)
        Task.NO_TASKS += 1
        return task