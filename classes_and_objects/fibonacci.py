def fibonacci(n):
    if n < 0:
        return "'n' must be a positive number"

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for num in range(1, 8):
    print(fibonacci(num))
