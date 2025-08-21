
"""
FIRST ASSIGNMENT 

Having aptech as your starting point, you are to direct a user to either of two locations: Abakpa or Emene


get your users name and the place they want to go

if they choose to go with the abakpa location, then direct them on how they can get there from aptech

if they choose to go with the emene location, then direct them on how they can also get there from aptech
"""

# first assignment answer 
name = input("hello what is your name")

#Ask where they ant to go to
destination = input(f"welcome {name}! where would you like to go (Abakpa or Emene)?").lower()

#Direct the user based on their choice
if destination == "abakpa":
  print(f"Alright {name}, here's how you can get to Abakpa from Aptech:")
  print("Take a bus from abakpa juntion towards new heaven.")
  print("from there join a bus going directly to abakpa")
  print("drop at abakpa main junction")

elif destination == "emene":
    print(f"Alright {name}, here's h0w you can get to eemene from aptech.")
    print("from aptech junction take a bus heading towards abakaliki road.")
    print("continue straight until you reach emene junction")
    print("from there you can stop at emene main bustop")
    

else:
    print(f"sorry {name}, that destination is not available. please choose either Abakpa or Emene!")




    """
    SECOND ASSIGNMENT 

It will be a game,
its called odd or even

you will ask the user for a number
the user will input a number
and the program has to say whether the number given is odd or even
    """

    # input() ask the user to type something
    # int()changess the input which is text into a number
    # % is the modulus operator - it gives the reminder after division
     # . if the number % 2 == 0, then its even.
     # . otherwise its odd.

# second assignment answer 
# ask the user to input the number

Number = int(input("enter a number: "))
# check if the number is even or odd

if Number % 2 == 0:
    print(f"The Number {Number} is EVEN")
else:
    print(f"The number {Number} is ODD")




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




"""
FOURTH ASSIGNMENT

Build a program that gives you the greater of two numbers
so the user will give you to numbers and
and the output should be the greater number
"""

# greater number

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

if num1 > num2:
    print("The greater nuber is:",num1)
elif num2 > num1:
    print("The greater number is:", num2)
else:
    print("both numbers are eual")