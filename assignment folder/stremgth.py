"""

for the third assignment
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password

"""

# Simple Password Strength Checker

while True:
    password = input("Enter a password: ")

    has_upper = False
    has_lower = False
    has_digit = False

    # check each character
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    # final check
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        print("Strong password ")
        break
    else:
        print("Weak password . Password must be at least 8 characters,")
        print("and include uppercase, lowercase, and a number.\n")