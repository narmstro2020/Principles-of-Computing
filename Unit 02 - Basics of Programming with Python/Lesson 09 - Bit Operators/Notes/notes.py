a = 12
b = 32
a_bin_text = bin(a)
b_bin_text = bin(b)
print(a)
print(a_bin_text)
print(b)
print(b_bin_text)

'''
| - bit operator or
& - bit operator and
^ - bit operator xor
>> bit shift right operator
<< bit shift left operator

'''

c = a | b
c_bin_text = bin(c)
print(c)
print(c_bin_text)

'''
a = 001100
b = 100000
c = 101100
| bit or is 1 if one of the columns is 1
'''

d = a & b
d_bin_text = bin(d)
print(d)
print(d_bin_text)

'''
a = 001100
b = 100000
d = 000000
& bit and is 1 if both of the columns is 1
'''

f = a ^ b
f_bin_text = bin(f)
print(f)
print(f_bin_text)

'''
a = 001100
b = 100000
f = 101100
^ bit xor is 1 if one or the other but not both of the columns is 1
'''

shift_right = a >> 2
shift_right_bin = bin(shift_right)
print(shift_right_bin)

shift_left = a << 3
shift_left_bin = bin(shift_left)
print(shift_left_bin)

opposite = ~a

'''
000000000000000000001100
111111111111111111110011

flip sign subtract 1
'''
print(opposite)