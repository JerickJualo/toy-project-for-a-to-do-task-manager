def super_menu(logged_acc):

    """
    Display the main interactive menu for a logged-in Account and route user choices
    to the appropriate account/task operations.

    This menu loops until the user chooses to log out. It provides options to:
      1. View account details
      2. View all tasks for the account
      3. Create a new task under the account
      4. Edit an existing task
      5. Log out and exit the menu loop

    Args:
        logged_acc (Account): The currently authenticated Account instance whose
                              data and tasks will be manipulated.

    Side Effects:
        - Prints menu prompts and separators to standard output.
        - Calls Account methods (full_acc_details, view_tasks, create_task).
        - Calls the edit_task() helper to handle task modifications.
    """

    print("\n=======================================================================================================================================================")
    print(f"Welcome back {logged_acc.username} to the To-Do Task Manager!")

    while True:
        print("\n=======================================================================================================================================================")
        print("\nPlease choose an option:")
        print("1. View Account Details")
        print("2. View Tasks")
        print("3. Create a New Task")
        print("4. Edit a Task")
        print("5. Log Out")
        print("========================================================================================================================================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Show full account info including all tasks
            print(logged_acc.full_acc_details())
        elif choice == "2":
            # List summary view of tasks
            print(logged_acc.view_tasks())
        elif choice == "3":
            # Prompt and create a new task under this account
            logged_acc.create_task()
        elif choice == "4":
            # Show tasks and then prompt for which task to edit
            print(logged_acc.view_tasks())

            edit_id = input("\nEnter the Task ID you want to edit:").strip()

            if int(edit_id) in logged_acc.tasks:
                edit_task(logged_acc, int(edit_id))
            else:
                print("Task ID not found.")
        
        elif choice == "5":
            # Exit the menu loop
            print("Logging out...")
            break


def edit_task(logged_acc, task_id):
    """
    Provide an interactive sub-menu for editing or deleting a single Task.

    Displays current task details (name, description, status, due date),
    then offers options to:
      1. Change the task's name
      2. Change the task's description
      3. Change the task's status
      4. Change the task's due date
      5. Delete the task entirely

    After the user selects an option, the corresponding Task or Account
    method is invoked to perform the change.

    Args:
        logged_acc (Account): The Account instance that owns the task.
        task_id (int):       The unique identifier of the Task to edit.

    Side Effects:
        - Prints detailed task information and edit prompts.
        - Calls Task.rename(), change_description(), change_status(),
          change_due_date(), or Account.delete_task() based on user input.
    """

    task = logged_acc.tasks[task_id]

    print("\n=======================================================================================================================================================")
    print(f"Editing Task: {task.task_name}")

    print("Current Task Details:")
    print(f"Name: {task.task_name}")
    print(f"Description: {task.description}")
    print(f"Status: {task.status}")
    print(f"Due Date: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'No due date set'}")

    print("=======================================================================================================================================================\n")

    
    print("Please choose an option to edit:")
    print("1. Change Task Name")
    print("2. Change Task Description")
    print("3. Change Task Status")
    print("4. Change Task Due Date")
    print("5. Delete Task")

    print("========================================================================================================================================================")

    edit_choice = input("Enter your choice (1-5): ").strip()

    if edit_choice == "1":

        print("=========================================================================================================================================================")
        new_name = input("Enter the new task name: ").strip()
        task.rename(new_name)

    elif edit_choice == "2":

        print("=========================================================================================================================================================")
        new_description = input("Enter the new task description: ").strip()
        task.change_description(new_description)

    elif edit_choice == "3":

        print("=========================================================================================================================================================")
        print("Please choose from: Not Started, In Progress, Completed, On Hold")
        new_status = input(f"Enter the new status for the task (current: {task.status}): ").strip()
        task.change_status(new_status)

    elif edit_choice == "4":
        # Delegate to the Task’s due-date setter

        task.change_due_date()

    elif edit_choice == "5":
        # Remove the task from both the Account and global registries
        logged_acc.delete_task(task_id)
        
    else:
        print("Invalid choice. Please try again.")