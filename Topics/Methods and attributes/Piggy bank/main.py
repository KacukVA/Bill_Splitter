from math import modf

class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = 1
        self.cents = 1

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents >= 100:
            result = str(self.cents / 100).split('.')
            self.dollars += int(result[0])
            self.cents = int(result[1])
