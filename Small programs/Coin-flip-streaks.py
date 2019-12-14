import random

number_of_streaks = 0
h_or_t = []
for experiment_number in range(1000):
    if random.randint(0,1) == 0:
        h_or_t.append("H")
    else:
        h_or_t.append("T")

    if ("H" and "H" and "H" and "H" and "H" and "H") in h_or_t or ("T" and "T" and "T" and "T" and "T" and "T") in h_or_t:
        number_of_streaks += 1

output = str(h_or_t).replace("'", "")
print(output)
print("Chance of streak: %s%%" % (number_of_streaks / 100))