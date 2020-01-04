from datetime import date, timedelta
from completion import Completion
import json

class Chore:
    def __init__(self, title, frequency):
        self.title = title
        self.frequency = frequency
        self.history = []

    def mark_completed(self, person):
        self.history.append(Completion(person, date.today().isoformat()))

    def get_last_completed_string(self):
        if self.history:
            last = self.history[-1]
            return f"{self.title} last completed on {last.day} by {last.person}"
        else:
            return f"{self.title} never completed"
    
    def get_delta_from_string(self, frequency):
        # Translates a human-readable string to a Python-friendly timedelta.
        # TODO: make this more robust or control the enumerations better
        
        if frequency is "daily":
            return timedelta(days=1)
        if frequency is "weekly":
            return timedelta(weeks=1)
        if frequency is "biweekly":
            return timedelta(weeks=2)
        if frequency is "monthly":
            # TODO: make this *actually* monthly
            return timedelta(weeks=4)
        if frequency is "annually":
            # TODO: account for leap years
            return timedelta(days=365)
    
    def get_last_completed_date(self):
        if self.history:
            return self.history[-1].day
    
    def get_next_due_date(self):
        if self.history:
            return date.fromisoformat(self.history[-1].day) + self.get_delta_from_string(self.frequency)
        else:
            # Not sure I like this.
            # TODO: Figure out a better way to handle next due date when
            #   history is empty
            return date.today() + self.get_delta_from_string(self.frequency)

    def get_next_due_date_string(self):
        return f"{self.get_next_due_date()}"

    def get_completed_by_tally(self):
        # !!!!!!!!!!!!!!!!!!!!!!!
        # TODO: Implement me!
        # Should return a list of tuples for the completer's names and the
        # number of times they have completed the task.
        # e.g. [("Alice", 3), ("Bob", 1)]
        return

    def toJSON(self):
        return json.dumps(self.__dict__)
