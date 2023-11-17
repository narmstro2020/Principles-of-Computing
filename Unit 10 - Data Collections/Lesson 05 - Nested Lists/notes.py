numbers = [1, 2, 3, 4]

countries = ['UK', 'US', 'Germany']

countries = [1, 'UK', 2, 'US']

# cells = [
#     # col0  col1  col2
#     ['A1', 'A2', 'A3'], # row 0
#     ['B1', 'B2', 'B3']  # row 1
# ]

# print(cells)

# print(cells[0])

# print(cells[0][0])

# print(cells[0][1])

# print(cells[1][2])

# cells = [
#     ['A1', 'A2', 'A3'], 
#     ['B1', 'B2', 'B3']
# ]
# for row in cells:
#     print("Row:", row)

# table = [
#     ['A1', 'A2', 'A3'], 
#     ['B1', 'B2', 'B3']
# ]

# for row in table:
#     for col in row:
#         print('Element:', col)

table = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3']
]
for row in table:
    for col in row:
        print(col, '', end='')
    print()

# #1 2 3 4 5
# #1 2 3 4 5
# #1 2 3 4 5
# #1 2 3 4 5

table = [
    [col for col in range(1, 6)]
    for row in range(4)
]
for row in table:
    for col in row:
        print(col, '', end='')
    print()
