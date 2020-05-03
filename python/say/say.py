def say(number):
    if number < 0 or number > 999999999999 or not isinstance(number, (int, float)):
        raise ValueError('error')
    import inflect
    e = inflect.engine()
    return e.number_to_words(number, andword='').replace(',', '')
