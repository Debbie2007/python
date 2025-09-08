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