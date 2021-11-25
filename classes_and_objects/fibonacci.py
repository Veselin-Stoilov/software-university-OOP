"""For loop fibonacci"""


def fib(n):
    a = 1
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a, b = b, c
            print(c)


fib(7)


"""Recursion fibonacci"""


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


