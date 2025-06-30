from datetime import datetime

#CLASS SECTION

class Task:

    statuses: list = ["Not Started", "In Progress", "Completed", "On Hold"]

    #Task Class Attributes
    ALL_TASKS: list = []
    NO_TASKS: int = 0
    LIST_TASK_ID: list[int] = []

    def __init__(self, task_name: str, description: str, status: str = "Not Started"):

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
        return f"Task(Task ID: '{self.task_id}', Task Name: '{self.task_name}',Description: '{self.description}')"


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
            
            print(f"Set the Due date of the task {self.task_name}: ")
            year = input("Enter the Year(eg. 2025): ").strip()

            while True:

                month_choice = input("""Enter the Month:
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
                    print("Invalid day, Please Enter a day within 31")
                    continue

                break
            
            self.due_date = datetime(int(year) if year.is_digit() else "Invalid Year Format", int(month_choice), day)
            print(f"{self.task_name} due date is now set!: {self.due_date}")

            return self.due_date
    


    @classmethod
    def create_task(cls):
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

        new_task = cls(task_name, description, task_status)

        print(f"""Task '{new_task.task_name}' created successfully with status '{new_task.status}'!
            Task_ID: {new_task.task_id}
            Description: {new_task.description}
            Date Created: {new_task.date_created.strftime('%Y-%m-%d %H:%M:%S')}
            Week Day Created: {new_task.date_created.strftime("%A")}""")
            
        new_task.day_created = new_task.date_created.strftime("%A")

        return new_task
    
# FUNCTION SECTION:
