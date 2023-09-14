'''
> : greater than
< : less than
>= : greater than or equal to
<= : less than or equal to.  
== :  equals be careful not to confuse this with the assignment operator =
!= : not equals
'''

grade_string = input("What is your grade? ")
grade = int(grade_string)

if grade < 0:
    print("You entered a grade that wasn't real")
elif grade < 5:
    print("You are an elementary school student")
elif grade < 9:
    print("You are a middle school student.")
elif grade <= 12:
    print("You are a high schooler")
else:
    print("You entered a grade that wasn't real")

