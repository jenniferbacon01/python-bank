from app.transaction import Transaction

class Bank(object):

    def __init__(self):
        self.transactions = []

    def receive(self, transaction):
        self.transactions.append(transaction)
