from money.money import Money
from money.currency import Currency


class Ksh(Money):

    CURRENCY = Currency.KES
    LOCALE = 'en_KE'

    def __init__(self, amount, *args):
        super(Ksh, self).__init__(amount, self.CURRENCY)

    def __str__(self):
        return self.format(self.LOCALE)
