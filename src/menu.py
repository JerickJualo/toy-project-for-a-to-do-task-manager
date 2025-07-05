def super_menu(logged_acc):

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
            print(logged_acc.full_acc_details())
        elif choice == "2":
            print(logged_acc.view_tasks())
        elif choice == "3":
            logged_acc.create_task()
        elif choice == "4":
            print(logged_acc.view_tasks())

            edit_id = input("\nEnter the Task ID you want to edit:").strip()

            if int(edit_id) in logged_acc.tasks:
                edit_task(logged_acc, int(edit_id))
            else:
                print("Task ID not found.")
        
        elif choice == "5":
            print("Logging out...")
            break


def edit_task(logged_acc, task_id):
    """
    Edit an existing task.
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

        task.change_due_date()

    elif edit_choice == "5":
            logged_acc.delete_task(task_id)
    else:
        print("Invalid choice. Please try again.")