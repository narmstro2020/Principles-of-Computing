def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])

print('The average is:', average)

# average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
# if average > 5.0:
#     print('The average is too high!')

# def get_average(input_numbers):
#     sum = 0.0
#     for number in input_numbers:
#         sum += number
#     average = sum / len(input_numbers)
#     return average
#     print('Show me!')

# average = get_average([2])

# print('The average is:', average)

def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return 
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False


print(is_first_last_equal([10, 20, 30, 40, 10]))

print(is_first_last_equal([10, 20, 30, 40, 50]))

print(is_first_last_equal([]))

