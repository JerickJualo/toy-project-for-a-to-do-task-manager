from datetime import datetime

#CLASS SECTION

class Task:

    statuses = ["Not Started", "In Progress", "Completed", "On Hold"]

    def __init__(self, task_name: str, description: str, status: str = "Not Started"):
        self.task_name = task_name
        self.description = description
        self.status = status
        self.date_created = datetime.now()
        self.due_date = None
        self.day_created = None


def set_due_date(self):
        month_list = {"1": "January", "2": "February", "3": "March", "4": "April", "5":"May", "6": "June",
                          "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
        
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


# FUNCTION SECTION:

def create_task():
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

    new_task = Task(task_name, description, task_status)

    print(f"""Task '{new_task.task_name}' created successfully with status '{new_task.status}'!
          Description: {new_task.description}
          Date Created: {new_task.date_created.strftime('%Y-%m-%d %H:%M:%S')}
          Week Day Created: {new_task.date_created.strftime("%A")}""")
          
    new_task.day_created = new_task.date_created.strftime("%A")