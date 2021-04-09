#!/usr/bin/env python3

"""
Exercism: Book store
Counts total price after discount
"""
from collections import Counter

def discounted(number: int, discounts: dict) -> float:
    """
    Counts discount rate
    """
    if discounts:
        if number > max(discounts.keys()):
            raise Exception
        return 1 - discounts[number]
    return 1

def price(number: int,
        discounts:dict={1:0, 2:0.05, 3:0.1, 4:0.2, 5:0.25},
        base_price:float=800) -> float:
    """
    Counts price for a few discounted items
    """
    return base_price * number * discounted(number, discounts)

def total(basket: list) -> float:
    """
    Counts price for all items
    """
    if len(basket) == 0:
        return 0
    if len(basket) == 1:
        return price(1)
    max_price = price(len(basket), discounts={})
    count = Counter(basket)
    discount_basket = [x for x,_ in count.most_common()]
    discount_number = 5
    max_range = len(discount_basket) if len(discount_basket) < 5 else 5
    for number in range(max_range, 1, -1):
        curr_basket = Counter(discount_basket[:number])
        temp_basket = count - curr_basket
        temp_basket_list = list(temp_basket.elements())
        cost = price(number) + total(temp_basket_list)
        if cost < max_price:
            max_price = cost
            basket = temp_basket_list
    return max_price

if __name__ == "__main__":
    print(total([1, 2, 3, 4, 5, 1, 6]))
    print(price(1))
