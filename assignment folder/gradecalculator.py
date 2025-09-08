"""
For the first assignment
Grade Calculator

Ask user for their score (0-100)
Assign letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
Provide encouraging messages based on the grade
Handle invalid input (scores outside 0-100 range)
"""

# Grade Calculator

# Ask user for their score (convert input to integer)
score = int(input("Enter your score (0-100): "))

# Handle invalid input
if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
else:
    # Determine grade
    if score >= 90:
        grade = "A"
        message = "Excellent work! Keep it up "
    elif score >= 80:
        grade = "B"
        message = "Great job! You're doing really well "
    elif score >= 70:
        grade = "C"
        message = "Good effort, but you can push a little harder "
    elif score >= 60:
        grade = "D"
        message = "You passed, but there’s room for improvement "
    else:
        grade = "F"
        message = "Please leave the calss you failed the course  "

    # Output result
    print(f"Your grade is: {grade}")
    print(message)