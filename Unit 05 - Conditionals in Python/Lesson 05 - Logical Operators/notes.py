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

python uses or  other languages use ||
python uses and other languages use &&
python uses not other languages use !
'''

age_string = input("What is your age? ")
age = int(age_string)

citizen_string = input("Are you a citizen (Enter nothing for False and Anything True)")
citizen = bool(citizen_string)

old_enough_for_pres = age >= 35
old_enough_for_congress = age >= 25

if old_enough_for_pres and citizen:
    print("You can run for president, senate, or congress")
elif old_enough_for_congress and citizen:
    print("You can run for congress only")
elif citizen:
    print("You are too young for office")
elif not citizen:
    print("You are not a citizen and cannot run")
