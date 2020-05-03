def is_isogram(string):
    punctuation = " ,_-"
    L = [x.lower() for x in string if x not in punctuation]
    for x in L:
        if L.count(x) > 1:
            return False
            break
    else:
        return True