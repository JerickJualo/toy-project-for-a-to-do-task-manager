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



    
