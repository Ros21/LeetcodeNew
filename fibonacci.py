def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.

    Args:
        n: The index of the Fibonacci number to calculate (non-negative integer).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 0:
        return 0  # Base case: The 0th Fibonacci number is 0
    elif n == 1:
        return 1  # Base case: The 1st Fibonacci number is 1
    else:
        # Recursive step: Sum of the two preceding Fibonacci numbers
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n_terms = 10  # Number of Fibonacci terms to generate

print("Fibonacci series using recursion:")
for i in range(n_terms):
    print(fibonacci_recursive(i))