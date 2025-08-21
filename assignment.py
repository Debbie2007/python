"""
This program demonstrates basic arithmetic operations
using two variables: addition, subtraction, multiplication, and division.
It prints out the results with descriptive text.
"""

# Define the two variables
num1 = 12
num2 = 4

# Addition
sum_result = num1 + num2
print(f"This is the sum of the two numbers: {sum_result}")

# Subtraction
sub_result = num1 - num2
print(f"This is the subtraction of the two numbers: {sub_result}")

# Multiplication
mul_result = num1 * num2
print(f"This is the multiplication of the two numbers: {mul_result}")

# Division
div_result = num1 / num2
print(f"This is the division of the two numbers: {div_result}")

"""
simpel calculator, that gets two user int inputs and op
returns sum, diff, uotient, product
"""
#user inputs, num1 and num2 

num1 = "int"("input your first number:")
num2 = "int"("input your second number:")

#operation input 
op = "input"("enter your operation: sum\nproduct \nuotient \ndiffernce").lower()

#sum, difference, uotient, product
sum = num1 + num2
differnce = num1 - num2
uotient = num1 / num2
product = num1 * num2

if (op.lower() == "sum"):
    print(f"this is the sum: {sum}")

elif (op.lower() == "difference"):
    print(f"this is the difference of the two numbets:{differnce}")

elif (op.lower() == "uotient"):
    if num2 == 0:
        print("undefined")
    
    else:
        print(f"this is the uotient of two numbers: {uotient}")

elif (op.lower() == "product"):
    print (f"this is the product of two numbers: {product}")

else:
    print("invalid opetrator")

print("end of program")




