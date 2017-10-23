import unittest
from app.bank import Bank

class TestBank(unittest.TestCase):

    def test_bank_add_method_returns_correct_result(self):
        bank = Bank()
        result = bank.add(2,2)
        self.assertEqual(4, result )

if __name__ == '__main__':
    unittest.main()
