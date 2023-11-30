# grades = {}
# print(grades)
# grades['John'] = 'A-'

# grades['Anne'] = 'B'

# print(grades)

# grades['Anne'] = 'A'

# print(grades)

# grades.update({'Charles': 'A'})

# print(grades)

# print(len(grades))

# if 'John' in grades:
#     print('John got:', grades['John'])

# del grades['John']
# print(grades)

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

# for el in grades:
#     print(el)

# for el in grades.keys():
#     print(el)

# for el in grades.values():
#     print(el)

# for item in grades.items():
#     print(item[0], "got", item[1])

for person, grade in grades.items():
    print(person, 'got', grade)


