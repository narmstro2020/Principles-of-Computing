'''
Print out what school they are in a student is based on input grade level

'''

grade_string = input("What is your grade? ")
grade = int(grade_string)

if grade >= 9 and grade <= 12:
    print("You are a high schooler.")
elif 