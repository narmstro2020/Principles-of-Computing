def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

nterms = 10

for i in range(nterms):
    print(fibonacci_recursive(i))