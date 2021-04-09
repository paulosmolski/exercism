def is_valid(isbn):
    isbn = [x for x in isbn if x in "X0123456789"]
    L = []
    for x in isbn:
        if x.isdigit():
            L.append(int(x))
        elif x == 'X' and isbn.index(x) == len(isbn)-1:
            L.append(10)
    if len(L) != 10: return False
    sum = 0
    for value, item in enumerate(L):
        sum += (10 - value) * item
    return sum % 11 == 0
    