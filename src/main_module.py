from classes_functs import log_in
from classes_functs import Account

# Introduction

print("""welcome to my To-Do List Manager
      
Coded by: Jerick C. Jualo""")

print("\n=======================================================================================================================================================")
print("Welcome to the To-Do Task Manager!")
print("=======================================================================================================================================================")
print("This program will help you track your goals and weekly schedule for Python, SQL Learning, and Math Study.")
print("Also, it will help you create your tasks for today and check the status of your tasks.")
print("Please log in to continue.")
print("=======================================================================================================================================================\n")


# Ensure the user is logged in before proceeding 
while not log_in():
        pass

print("\n=======================================================================================================================================================")
print(f"Here's Jerick's Goals for this Summer Vacation")
print("=======================================================================================================================================================")
print("Goals:")
print("1. Solidify Python skills from Basic to Data Collections to Functions to File and Error Handling to OOP")
print("2. Learn PostgreSQL")
print("3. Study Math/Statisticxs for Data Science At least Study and Solidify my Math Skills in Algebra")
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

