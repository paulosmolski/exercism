def flatten(iterable):
    a = []
    for x in iterable:
        if x == None:
            continue
        elif not isinstance(x, (list, tuple)):
            a.append(x)
        else:
            a.extend(flatten(x))
    return a        
