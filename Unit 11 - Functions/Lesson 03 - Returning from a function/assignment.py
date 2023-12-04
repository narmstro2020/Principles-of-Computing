def get_median_odd(numbers, count):
    index_median = count // 2
    ##YOU DO return the median from numbers using [index_median]


def get_median_even(numbers, count):
    index_middle2 = count // 2
    index_middle1 = index_middle2 - 1
    middle1 = numbers[index_middle1]
    middle2 = numbers[index_middle2]
    median = (middle1 + middle2) / 2
    ##YOU DO:  return the median 

def get_median(numbers):
    numbers.sort()
    count = len(numbers)
    if count % 2 == 0:
        return get_median_even(numbers, count)
    else:
        return get_median_odd(numbers, count)


list1 = [5, 3, 2, 1, 4]
median1 = get_median(list1)
print("The median of list1 is", median1)
list2 = [5, 3, 2, 1]
median2 = get_median(list2)
print("The median of list2 is", median2)
