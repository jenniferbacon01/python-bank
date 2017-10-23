class Transaction(object):

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def is_a_credit(self):
        if self.amount > 0:
            return True
        else:
            return False
