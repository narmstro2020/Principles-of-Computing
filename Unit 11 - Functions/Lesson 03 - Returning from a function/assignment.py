def get_median_odd(numbers, count):
    index_median = count // 2
    return numbers[index_median]


def get_median_even(numbers, count):
    index_middle2 = count // 2
    index_middle1 = index_middle2 - 1
    middle1 = numbers[index_middle1]
    middle2 = numbers[index_middle2]
    median = (middle1 + middle2) / 2
    #YOU DO.  Make this function return something.  You know the median.  


def get_median(numbers):
    numbers.sort()
    count = len(numbers)
    if count % 2 == 0:
        median = get_median_even(numbers, count)
        return median
    else:
        #YOU do this part.  Have this else block return the median as determined by get_median_odd(numbers, count)
        pass  #REMOVE THIS PASS WHEN YOU ARE DONE WITH YOUR PART

list1 = [5, 3, 2, 1, 4]
median1 = get_median(list1)
print("The median of list1 is", median1, ".")
list2 = [5, 3, 2, 1]
median2 = get_median(list2)
print("The median of list2 is", median2, ".")
