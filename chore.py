from collections import namedtuple
from datetime import date, timedelta

Completion = namedtuple('Completion', 'person day')

class Chore:
    def __init__(self, title, frequency):
        self.title = title
        self.frequency = self.get_delta_from_string(frequency)
        self.history = []

    def mark_completed(self, person):
        self.history.append(Completion(person, date.today()))

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
            return self.history[-1].day + self.frequency
        else:
            # Not sure I like this.
            # TODO: Figure out a better way to handle next due date when
            #   history is empty
            return date.today() + self.frequency

