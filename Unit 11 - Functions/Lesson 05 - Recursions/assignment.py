def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

nterms = 1000000

for i in range(nterms):
    print("Fib number", i, ":", fibonacci_recursive(i))