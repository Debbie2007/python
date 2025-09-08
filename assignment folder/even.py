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
