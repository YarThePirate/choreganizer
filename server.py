from chore import Chore
from datetime import date, timedelta

class Scheduler:
    
    def __init__(self, data_src):
        self.chores = self.load(data_src)

    def load(self, data_src):
        # should take a URL or raw file... for now, just return source
        return data_src

    def get_chores_due(self):
        return [ chore.title for chore in self.chores if chore.get_next_due_date() < date.today() ]
