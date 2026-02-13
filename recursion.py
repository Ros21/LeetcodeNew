def factorial(n):
    print(f"{n}")
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(4))