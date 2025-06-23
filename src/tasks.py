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