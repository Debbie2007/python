"""
for the fourth assignment
A Very Simple Student Grade Tracker

Create a dictionary where keys are student names and values are lists of their test scores
Add functions to:

Add a new student
Add a grade for existing student
Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table

"""


# Student Grade Tracker

students = {}   # empty dictionary

# add students and grades
students["Alice"] = [85, 90]
students["Bob"] = [70, 80]

# calculate averages
for name in students:
    grades = students[name]
    avg = sum(grades) / len(grades)
    print(name, "grades:", grades, "average:", avg)

# find top student
top_name = ""
top_avg = 0
for name in students:
    avg = sum(students[name]) / len(students[name])
    if avg > top_avg:
        top_avg = avg
        top_name = name

print("Top student:", top_name, "with average:", top_avg)