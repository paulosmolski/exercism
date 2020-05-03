def abbreviate(words):
    acrolist = []
    for item in words:
        if item not in ('!','.',':', '_', '-'):
            acrolist.append(item)
        else:
            acrolist.append(" ")
    words = "".join(acrolist)
    words = words.upper().split()
    acronym = [x[0] for x in words]
    acronym = "".join(acronym)
    return acronym