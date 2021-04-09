def prime(number):
    if number <= 0:
        raise ValueError("Wrong value")
    pr = gen_prime()
    out = 0
    for x in range(number + 1):
        out = next(pr)
    return out


def is_prime(number):
    if number <= 0:
        return False
    elif number == 1 or number == 2:
        return True
    for x in range(2, number):
        if number % x == 0:
            return False
            break
    else:
        return True

def gen_prime():
    for x in range(1000000):
        if is_prime(x):
            yield x

