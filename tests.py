import unittest
from datetime import date, timedelta

from chore import *

class ChoreTestMethods(unittest.TestCase):

    test_no_history = Chore("Test Empty", "weekly")
    
    test = Chore("Test", "weekly")
    test.history.append(Completion("Alice", "2019-11-25"))
    test.history.append(Completion("Bob", "2019-12-30"))

    def test_title_is_string(self):
        #test = Chore("Test Non Empty", "weekly")
        self.assertTrue(isinstance(self.test.title, str))
    
    def test_frequency_is_string(self):
        self.assertTrue(isinstance(self.test.frequency, str))
        self.assertFalse(isinstance(self.test.frequency, timedelta))

    def test_next_due_date_is_date(self):
        self.assertTrue(isinstance(self.test.get_next_due_date(), date))
    
    def test_next_due_date_string_is_string(self):
        self.assertTrue(isinstance(self.test.get_next_due_date_string(), str))

    def test_JSON_returns_valid_string(self):
        json_string = '{"title": "Test", "frequency": "weekly", "history": [["Alice", "2019-11-25"], ["Bob", "2019-12-30"]]}'
        self.assertEqual(self.test.toJSON(), json_string)

    def test_returns_correct_next_due_date(self):
        with_history = self.test.get_next_due_date_string()
        without_history = self.test_no_history.get_next_due_date_string()
        today_plus_one_week = date.today() + timedelta(days=7)

        self.assertEqual(with_history, "2020-01-06")
        self.assertEqual(without_history, f"{today_plus_one_week}")

if __name__ == "__main__":
    unittest.main()