import math
def classify(number):
    if number <= 0:
        raise ValueError("Sth")
    maxdiv = math.floor(number/2)
    aliquot = 0
    for x in range(1, maxdiv+1):
        if number % x == 0:
            aliquot += x
    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"

print(classify(28))