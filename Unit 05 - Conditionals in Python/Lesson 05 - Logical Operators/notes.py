'''
    Boolean (Logical) Operators

    unary
    not: 

    binary 
    and: 
    or: 

    not True = False
    not False = True

    a_boolean = True
    not a_boolean :  equal False

And Truth Table
    True and True = True
    True and False = False
    False and True = False
    False and False = False

Or Truth Table
    True or True = True
    True or False = True
    False or True = True
    False or False = False
'''

age_string = input("What is your age? ")
age = int(age_string)

citizen_string = input("Are you a citizen (Enter nothing for False and Anything True)")
citizen = bool(citizen_string)

age_test_for_pres_and_senate = age >= 35
age_test_for_congress = age >= 25

if age_test_for_pres_and_senate and citizen:
    print("You can run for president, senate, or congress")
elif age_test_for_congress and citizen:
    print("You can run for congress only")
elif citizen:
    print("You are too young for office")
elif not citizen:
    print("You are not a citizen and cannot run")
