import random

def roll_until_5_followed_by_six_shows_up():
    count = 0
    rolls = []
    while True:
        roll = random.randint(1, 6)
        rolls.append(roll)
        if len(rolls) >= 2 and rolls[-2] == 5 and rolls[-1] == 6:
            break
        else:
            count += 1

    return count

def roll_until_5_followed_by_5_shows_up():
    count = 0
    rolls = []
    while True:
        roll = random.randint(1, 6)
        rolls.append(roll)
        if len(rolls) >= 2 and rolls[-2] == 5 and rolls[-1] == 5:
            break
        else:
            count += 1
    return count

def number_of_times_for_roll(n):
    count_5_6 = 0
    count_5_5 = 0
    for _ in range(n):
        count_5_6 += roll_until_5_followed_by_six_shows_up()
        count_5_5 += roll_until_5_followed_by_5_shows_up()
    return count_5_6, count_5_5

n = 1000
count_5_6, count_5_5 = number_of_times_for_roll(n)
print(f"Average number of rolls to get 5 followed by 6: {count_5_6 / n}")
print(f"Average number of rolls to get 5 followed by 5: {count_5_5 / n}")