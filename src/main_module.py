print("""welcome to my To-Do List Manager
      
Coded by: Jerick C. Jualo""")

username = input("\nEnter your username: ")
password = input("Enter your password: ")

if username.lower() in "jerick":
    if password.lower() in "jualo":
        print(f"\nWelcome back, {username}!")

else:
    print("Exiting the program. Please run again with the correct username.")
    exit()

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

     
# use the function f-string and variable task_project_python to get its string value
# use the function f-string and variable task_sql to get its string value