def print_median_odd(numbers: list[int], count: int):
    index_median: int = count // 2
    print("The median of the list is", numbers[index_median])


def print_median_even(numbers: list[int], count: int):
    index_middle2: int = count // 2
    index_middle1: int = index_middle2 - 1
    middle1: int = numbers[index_middle1]
    middle2: int = numbers[index_middle2]
    median: float = (middle1 + middle2) / 2
    print("The median of the list is", median)


def print_median(numbers : list[int]):
    numbers.sort()
    count: int = len(numbers)
    if count % 2 == 0:
        print_median_even(numbers, count)
    else:
        print_median_odd(numbers, count)


list1: list[int] = [5, 3, 2, 1, 4]
print_median(list1)
list2: list[int] = [5, 3, 2, 1]
print_median(list2)

