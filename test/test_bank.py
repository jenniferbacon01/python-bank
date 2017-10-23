import unittest
from app.bank import Bank
from doubles import ObjectDouble, allow

class TestBank(unittest.TestCase):

    def test_bank_can_receive_a_transaction(self):
        transaction = ObjectDouble('app.Transaction')
        # allow(transaction).receive
        bank = Bank()
        bank.receive(transaction)
        self.assertEqual(bank.transactions[0], transaction )

if __name__ == '__main__':
    unittest.main()
