import random

number_of_streaks = 0
h_or_t = []
for experiment_number in range(101):
    if random.randint(0,1) == 0:
        h_or_t.append("H")
    else:
        h_or_t.append("T")
output = str(h_or_t).remove("'")
print(1)