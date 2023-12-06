# factorial
# 3! = 3 * 2 * 1 = 6
# 3! = 3 * 2!
# 3! = 3 * 2 * 1!
# 3! = 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1  = 120
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# iterative
def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial

print(get_factorial(1000))

def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number - 1)

print(get_factorial_recursive(1000))

