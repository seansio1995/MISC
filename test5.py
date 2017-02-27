import random
def yield_dates():
    for i in range(5):
        date = random.choice(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
        yield date


print(yield_dates())
print(next(yield_dates()))
print(next(yield_dates()))
print(next(yield_dates()))
print(next(yield_dates()))
print(next(yield_dates()))
