'''
What you know now.  

Basics of Variables
Variable Reassignment.  Doesn't matter type or value in python.
Assignment Operator: =, assigns values to variables
Print function: print(objects), prints the items to the terminal.
Type function: type(object), returns or gives us the type of the objects
8 mathematical operators listed below
'''
age = 42
print(age)
age = 43
print(age)
age="Forty-two"
print(age)


'''
Mathematical Operators
binary
+: Addition
-: Subtraction
*: Multiplication
/: Division
**: Exponentiation (powers)
//: Integer Division
% : Modulus 

unary
-: Unary minus
'''

'''
Mathematical Assignment Operators
+=: Addition Assignment
-=: Subtraction Assignment
*=: Multiplication Assignment
/=: Division Assignment
**=: Exponentiation (powers) Assignment
//=: Integer Division Assignment
%=: Modulus Assignment
'''

sum = 34 + 42
print("The sume of 34 and 42 is: ", sum)
difference = 42 - 34
print("The difference of 42 and 34 is: ", difference)
a = 34
b = 42
product = a * b
print("The product of a and b is: ", product)
quotient = a / b
print("The quotient of a and b is: ", quotient)

# b = 0
# quotient = a / b
# print("The quotient of a and b is: ", quotient)

c = 7
d = 4
powered = c ** d
print(powered)

int_division = c // d
print(int_division)

f = 5
f = -f
print(f)

#What the heck is modulus (%)
# remainder after division.  
# 5 / 2 = 2 R1 = 2.5


# 7 / 4 = 1 R 3
modulus = c % d
print(modulus)
# should give me 3

quotient = c // d
remainder = c % d

print("c divided by d with remainders is: ", quotient, "R", remainder)

a = 5
a = a + 1
b = 7
a = a + b

a = 5
a += 1

a -= 1



