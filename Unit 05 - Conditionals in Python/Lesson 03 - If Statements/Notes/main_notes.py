answer = bool(input("Are you 35 years old or older (False (just hit enter), True anything): "))

print(type(answer))

print(answer)

'''
if condition:
    behavior if true
    ...
    ...


'''


if (answer):
    print("Congratulations you can run for the presidency")
    print("Congratulations you can run for the presidency")

else:
    print("Unfortunately you cannot run for president")


'''

Falsy

Empty Lists []

Empty tuples ()
Empty dictionaries {}
Empty sets set()
Empty strings ""
Empty ranges range(0)

Integer 0
Float 0.0
Complex 0j

Constants
None
False

Everything else evaluates to true

'''


grade = int(input("What grade level are you"))

over_ten = grade > 10

ten = grade == 10

under_ten = grade < 10

if over_ten:
    print("You are past grade 10.  No ice cream")
elif ten:
    print("You are a 10th grade.  You get ice cream")
else:
    print("You are not yet a 10th grader.  No ice cream")


