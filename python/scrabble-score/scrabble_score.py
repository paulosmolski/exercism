def score(word):
    points = {}
    points.update({x : 1 for x in "AEIOULNRST"})
    points.update({x : 2 for x in "DG"})
    points.update({x : 3 for x in "BCMP"})
    points.update({x : 4 for x in "FHVWY"})
    points['K'] = 5
    points.update({x : 8 for x in "JX"})
    points.update({x : 10 for x in "QZ"})
    word = word.upper()
    sum = 0
    for x in word:
        sum += points[x]
    return sum
