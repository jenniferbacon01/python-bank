import unittest
from app.bank import Bank

class TestBank(unittest.TestCase):

    def test_bank_can_receive_a_transaction(self):
        bank = Bank()
        result = bank.add(2,2)
        self.assertEqual(4, result )

if __name__ == '__main__':
    unittest.main()
