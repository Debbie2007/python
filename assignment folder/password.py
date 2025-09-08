"""
THIRD ASSIGNMENT 

Build a simple password checker.

If the password the user inputs isnt “MR FRANK”
tell them access denied
if  the inputs matches “MR FRANK”
tell them access given??
"""

# simple password checker

password = input("Enter password")
if password == "MR FRANK":
    print("acess given")

else:
    print("acess denied??")
