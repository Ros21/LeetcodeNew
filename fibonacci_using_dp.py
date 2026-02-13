def fibonacci_dp(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Print the Fibonacci series
n = 10
series = [fibonacci_dp(i) for i in range(n)]
print(series)
