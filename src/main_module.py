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

    
print("==========================")
print("Heres my Everday Tasks for this Summer Vacation")
print("==========================")
print("Goals:")
print("1. Solidify my Python skills from Basic to Data Collections to Functions to File and Error Handling to OOP")
print("2. Learn PostgreSQL")
print("3. Study Math/Statistics for Data Science At least Study and Solidify my Math Skills in Algebra")
print("==========================")

print("Starting June 1, 2025, Here's the Main Task that i will do Everday:")
print("""
Sunday - Do the Toy Projects in Python
       
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
         - Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT""")
         
 # i change the rotation of tasks from monday to saturday and only sunday is the toy project in python
 # as i now relized that i need to rest and only do the toy projects in python on sunday
 

task_learn_python = "Do the Toy Projects in Python in Morning and Afternoon"
task_project_python = "Study/Code in Python or Do Problem Solving in Python Problems provided by ChatGPT or HackerRank, LeetCode, Codewars"
task_math = "Study Math (Getting Ready for Algebra Course in Khan Academy)"
task_sql = "Study SQL/PostgreSQL and Do Problem Solving in SQL Problems provided by ChatGPT"

print("==========================")
print("\nToday's Task Finder")
print("==========================")
print("What Month is Today?")
print("- May")
print("What Day is Today?")
print("- 31\n")
print("The date is May 31, 2025 is Saturday")
print("======Today's Tasks ======")

print(f"""
 Do the Saturday Tasks:
 1. {task_project_python}  
 2. {task_sql}             
     """)
     
# use the function f-string and variable task_project_python to get its string value
# use the function f-string and variable task_sql to get its string value