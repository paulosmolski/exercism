def find_anagrams(word, candidates):
    output = []
    for item in candidates:
        if sorted(item.lower()) == sorted(word.lower()) and item.lower() != word.lower():
            output.append(item)
    return output