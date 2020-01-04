import unittest
from datetime import date, timedelta

from chore import *
from server import Scheduler
from dummydata import *

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

    def test_returns_correct_completion_tally_for_person(self):
        self.assertEqual(garbage.get_completed_tally_for("Alice"), 3)
        self.assertEqual(garbage.get_completed_tally_for("Bob"), 1)
    
    def test_returns_correct_date_last_completed_by_person(self):
        self.assertEqual(garbage.get_date_last_completed_by("Alice"), "2020-01-01")
        self.assertEqual(garbage.get_date_last_completed_by("Bob"), "2019-12-18")

    def test_returns_correct_completion_tallies(self):
        garbage_totals = { "Alice": 3, "Bob": 1 }
        litter_totals = { "Bob": 5 }
        dog_food_totals = { "Alice": 2, "Bob": 1 }
        self.assertEqual(garbage.get_completed_by_tallies(), garbage_totals)
        self.assertEqual(litter.get_completed_by_tallies(), litter_totals)
        self.assertEqual(dog_food.get_completed_by_tallies(), dog_food_totals)


class SchedulerTests(unittest.TestCase):

    def test_scheduler_loads_data_correctly(self):
        self.assertTrue(dummy_scheduler.chores is dummy_chores)
        self.assertEqual(len(dummy_scheduler.chores[0].history), 4)
    
    def test_scheduler_returns_correct_chores_due(self):
        self.assertEqual(dummy_scheduler.get_chores_due(), ["Litter Boxes"])
        hold = dummy_scheduler.chores[2].history.pop()
        self.assertEqual(dummy_scheduler.get_chores_due(), ["Litter Boxes", "Buy Dog Food"])
        dummy_scheduler.chores[2].history.append(hold)

if __name__ == "__main__":
    unittest.main()