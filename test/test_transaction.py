import unittest
from app.transaction import Transaction

class TestBank(unittest.TestCase):

    def test_transaction_can_be_instantiated_with_date_and_amount(self):
        transaction = Transaction("23/10/17", 100)
        self.assertEqual(transaction.date, "23/10/17" )
        self.assertEqual(transaction.amount, 100 )

if __name__ == '__main__':
    unittest.main()
