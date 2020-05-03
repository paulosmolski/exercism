class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
    def transformation(self):
        transform = lambda x : x * 2 if x * 2 <= 9 else x * 2 - 9
        oldnum = self.card_num.replace(" ", "")
        if len(oldnum) <= 1 or not oldnum.isdigit():
            return None
        oldnum = [int(x) for x in oldnum]
        if len(oldnum) % 2 == 0:
            return [transform(i) if v % 2 == 0 else i for v, i in enumerate(oldnum)]
        else:
            return [i if v % 2 == 0 else transform(i) for v, i in enumerate(oldnum)]
    def valid(self):
        x = self.transformation()
        if x:
            return sum(x) % 10 == 0
        else:
            return False
    def __bool__(self):
        return self.valid()

def can_pay(card_num: str):
    card_num = Luhn(card_num)
    if card_num:
        print("You can pay")
    else:
        print("You can't pay")

