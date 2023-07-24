'''
str() -> converts whatever your variable is to text
int() -> this converts text to integers.  + or - whole numbers
float() -> this converts text to decimal numbers + or -
'''

age_text = "42"
print(type(age_text))
age_int = int(age_text)
print(age_int)
print(type(age_int))
age_float = float(age_text)
print(age_float)
print(type(age_float))

'''

Simple height converted feet and inches to meters

'''

feet = int(input("How many feet tall are you? "))
inches = int(input("How many inches above the feet tall are you? "))
inches_to_meters = 0.0254
total_inches = feet * 12 + inches
total_meters = total_inches * inches_to_meters
print("Your height is", feet, "feet", inches, "inches")
print("Your height is", total_inches, "inches")
print("Your height is", total_meters, "meters")

feet_as_text = str(feet)
print(type(feet_as_text))


