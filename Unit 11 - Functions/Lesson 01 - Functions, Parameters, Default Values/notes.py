# def greet():
#     print('Hello, my dear!')

# greet()
# greet()


# def get_average(input_numbers):
#     sum = 0.0
#     for number in input_numbers:
#         sum += number
#     average = sum / len(input_numbers)
#     print(average)

# get_average([5.0, 3.5, 7.8, 9.9, 10.0])
# get_average([3, 2, 1, 0, -1, -2, -3, 520])

# get_average()

#get_average(5)

# def print_letter_count(text, letter):
#     counter = 0
#     for char in text:
#         if char == letter:
#             counter += 1
#     print('Number of', letter, 'is', counter)

# print_letter_count('Welcome', 'e')

# print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')

# print_letter_count('e', 'Welcome')

# print_letter_count(text='Welcome', letter='e')

# print_letter_count(letter='e', text='Welcome')

# print('Hello', 'How are you?', end='.', sep='-')

def print_letter_count(text='This is the default string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# print_letter_count('How many letters a are here?')

# print_letter_count()

# print_letter_count('Search here', letter='a')

# # #Python
# def greet():
#     print("Hi There")

# # #JavaScript
# function greet(){
#     console.log("Hi There");
# }

# # #C
# void greet(){
#     puts("Hi There");
# }

# # #C++
# void greet(){
#     cout << "Hi There" << endl;
# }

# # #C#
# public void greet(){
#     Console.Writeline("Hi There");
# }

# # #Java
# public void greet(){
#     System.out.println("Hi There");
# }
