from chore import Chore
from completion import Completion
from server import Scheduler


dummy_chore_no_history = Chore("Test Empty", "weekly")
    
dummy_chore = Chore("Test", "weekly")
dummy_chore.history.append(Completion("Alice", "2019-11-25"))
dummy_chore.history.append(Completion("Bob", "2019-12-30"))

garbage = Chore("Take Out Garbage", "weekly")
garbage.history = [
    Completion("Alice", "2019-12-11"),
    Completion("Bob", "2019-12-18"),
    Completion("Alice", "2019-12-24"),
    Completion("Alice", "2020-01-01")  # End Chore 0: index 3
]

litter = Chore("Litter Boxes", "daily")
litter.history = [
    Completion("Bob", "2019-12-22"),
    Completion("Bob", "2019-12-23"),
    Completion("Bob", "2019-12-24"),
    Completion("Bob", "2019-12-25"),
    Completion("Bob", "2019-12-26")    # End Chore 1: index 8
]

dog_food = Chore("Buy Dog Food", "monthly")
dog_food.history = [
    Completion("Alice", "2019-11-01"),
    Completion("Bob", "2019-12-02"),
    Completion("Alice", "2020-01-01")   # End Chore 2: index 11
]

dummy_chores = [garbage, litter, dog_food]

dummy_scheduler = Scheduler(dummy_chores)