from classes_functs import log_in
from classes_functs import account


print("""welcome to my To-Do List Manager
      
Coded by: Jerick C. Jualo""")

print("\n=======================================================================================================================================================")
print("Welcome to the To-Do Task Manager!")
print("=======================================================================================================================================================")
print("This program will help you track your goals and weekly schedule for Python, SQL Learning, and Math Study.")
print("Also, it will help you create your tasks for today and check the status of your tasks.")
print("Please log in to continue.")
print("=======================================================================================================================================================\n")

log_in()

username = input("\nEnter your username: ")
password = input("Enter your password: ")

if username.lower() in "jerick":
    if password.lower() in "jualo":
        print(f"\nWelcome back, {username}!")

else:
    print("Exiting the program. Please run again with the correct username.")
    exit()
    
print("\n=======================================================================================================================================================")
print(f"Here's {username}'s Goals for this Summer Vacation")
print("=======================================================================================================================================================")
print("Goals:")
print("1. Solidify Python skills from Basic to Data Collections to Functions to File and Error Handling to OOP")
print("2. Learn PostgreSQL")
print("3. Study Math/Statistics for Data Science At least Study and Solidify my Math Skills in Algebra")
print("=======================================================================================================================================================")

weekly_schedule = input("\nDo you want to see the Weekly Schedule for Python, SQL Learning and Math Study? (yes/no): ").strip().lower()

if weekly_schedule == "yes":
       print("\nHere's the Weekly Schedule for Python, SQL Learning and Math Study")
       print("=======================================================================================================================================================")
       print("""
       Sunday - Do the Toy Projects in Python
              - Rest and Relax
       
       Monday - Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars
              - Study Math(Getting Ready for Algebra Course in Khan Academy)
       
       Tuesday - Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars
               - Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT

       Wednesday - Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars
                 - Study Math(Getting Ready for Algebra Course in Khan Academy)
      
       Thursday - Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars
                - Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT

       Friday - Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars
              - Study Math(Getting Ready for Algebra Course in Khan Academy)

       Saturday - Do the Toy Projects in Python 
                - Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT\n""")
       print("=======================================================================================================================================================\n")
         
 # i change the rotation of tasks from monday to saturday and only sunday is the toy project in python
 # as i now relized that i need to rest and only do the toy projects in python on sunday


month = input("What Month is Today?: ").strip().lower()
day = input("What Day is Today?: ").strip().lower()
week_day = input("What Day of the Week is Today?: ").strip().upper()
print("\n=======================================================================================================================================================")
print(f"Today's Date: {month} {day}, 2025 and it is a {week_day}")
print("=======================================================================================================================================================\n")


task_learn_python = "Do the Toy Projects in Python in Morning and Afternoon"
task_project_python = "Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars"
task_math = "Study Math (Getting Ready for Algebra Course in Khan Academy)"
task_sql = "Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT"

if week_day == "SUNDAY":
    print(f"""\nToday's Task: 1. {task_learn_python}
               2. Rest and Relax""")
elif week_day == "MONDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
               2. {task_math}""")
elif week_day == "TUESDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
              2. {task_sql}""")
elif week_day == "WEDNESDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
              2. {task_math}""")
elif week_day == "THURSDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
              2. {task_sql}""")
elif week_day == "FRIDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
              2. {task_math}""")
elif week_day == "SATURDAY":
       print(f"""\nToday's Task: 1. {task_learn_python}
              2. {task_sql}""")
              

print("\nStatus of Today's Task:")
print("""Task 1: COMPLETED(X)
        ON GOING(Y)
        FAILED(Z)\n""")
        
task1_status = input("\nTask 1 Status: ").upper()

if task1_status == "X":
    print("\nGreat and Good Job! How about the Task 2?\n")
elif task1_status == "Y":
    print("\nKeep Going! You can do it!\n")
elif task1_status == "Z":
    print("\nIt's Okay, You can do it next time, Don't Worry!\n")
    
task2_status = input("Task 2 Status: ").upper()

if task2_status == "X":
    print("\nGreat and Good Job!\n")
elif task2_status == "Y":
    print("\nKeep Going! You can do it!\n")
elif task2_status == "Z":
    print("\nIt's Okay, You can do it next time, Don't Worry!\n")
    
    
if task1_status and task2_status == "X":
    print("\n\nCongratulations, You DID IT!, STAY GRINDING and Another step towards to our Dreams.")
    
elif task1_status or task2_status == "Y":
    print("\n\nLock In! and dont forget to take a rest time to time.")
    
elif task1_status or task2_status == "Z":
    print("\n\nIts okay, Failure is the mother of learning, try again tomorrow!")
    
    
