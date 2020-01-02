from chore import Chore

test = Chore("testChore", "weekly")
test.mark_completed("freddy")

print(test.get_last_completed_string())