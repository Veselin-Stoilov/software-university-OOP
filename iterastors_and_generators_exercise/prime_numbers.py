from math import sqrt


def get_primes(integers):
    for n in integers:
        is_prime = True
        if n > 1:
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))