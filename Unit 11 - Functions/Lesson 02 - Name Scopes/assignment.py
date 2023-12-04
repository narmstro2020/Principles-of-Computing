def print_median_odd(numbers, count):
    index_median = count // 2
    print("The median of the list is", numbers[index_median])


def print_median_even(numbers, count):
    index_middle2 = count // 2
    index_middle1 = index_middle2 - 1
    middle1 = numbers[index_middle1]
    middle2 = numbers[index_middle2]
    median = (middle1 + middle2) / 2
    print("The median of the list is", median)


def print_median(numbers):
    numbers.sort()
    count = len(numbers)
    if count % 2 == 0:
        print_median_even(numbers, count)
    else:
        print_median_odd(numbers, count)


list1 = [5, 3, 2, 1, 4]
print_median(list1)
list2 = [5, 3, 2, 1]
print_median(list2)

