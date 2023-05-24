def factorial_function(n):
    if n < 2:
        return 1
    return n * factorial_function(n - 1)