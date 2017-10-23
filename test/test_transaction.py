import unittest
from app.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def test_transaction_can_be_instantiated_with_date_and_amount(self):
        transaction = Transaction("23/10/17", 100)
        self.assertEqual(transaction.date, "23/10/17" )
        self.assertEqual(transaction.amount, 100)


    def test_transaction_can_calculate_if_credit(self):
        transaction = Transaction("23/10/17", 100)
        self.assertTrue(transaction.is_a_credit())

    def test_transaction_can_calculate_if_not_credit(self):
        transaction = Transaction("23/10/17", -100)
        self.assertFalse(transaction.is_a_credit())

if __name__ == '__main__':
    unittest.main()
