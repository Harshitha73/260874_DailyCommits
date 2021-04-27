def get_primes():
    x = 2
    while x < 10:
        if is_prime(x):
            yield x
        x += 1


def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


for i in get_primes():
    print(i)
