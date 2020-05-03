def decode(string):
    if not string:
        return ""
    prevchar = ""
    out = ""
    count = 1
    for x in string:
        if x.isdigit() and not prevchar.isdigit():
            count = int(x)
        elif x.isdigit() and prevchar.isdigit():
            count = int(str(count) + x)
        else:
            out += count * x
            count = 1
        prevchar = x
    return out

def encode(string):
    if not string:
        return ""
    prevchar = ""
    out = ""
    count = 1
    for char in string:
        if char == prevchar:
            count += 1
        elif count == 1:
            out += prevchar
        else:
            out += str(count) + prevchar
            count = 1
        prevchar = char
    if count == 1:
        out += prevchar
    else:
        out += str(count) + prevchar
    return out
