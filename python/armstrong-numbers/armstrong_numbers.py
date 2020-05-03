def is_armstrong_number(number):
    digits = [int(x) for x in str(number)]
    value = 0
    for x in digits:
        value += x ** len(digits)
    return value == number

