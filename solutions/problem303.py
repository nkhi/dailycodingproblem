# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

# Bonus: When, during the course of a day, will the angle be zero?

# Interpretation: A circle has 2pi radians, or ~360. degree between subsequent hour markers (1 to 2)
#                 would be 360 / 12 * (2-1) = 30 deg
#                 Will get the degree of the hour hand, of the min hand, and then find the diff depending on the min

def hour_degree(hour: str) -> int:
    "Returns the degree of the hour hand relative to noon on a clockface"
    if int(hour) >= 1 and int(hour) <= 12:
        return int(hour) * 30

def min_degree(mins: str) -> float:
    "Returns the degree of the minute hand relative to noon on a clockface"
    if int(mins) >= 0 and int(mins) <= 60:
        return int(mins) * 6

def get_degree_from_mins(time: str) -> float:
    "Return the degree between the minute and hour hands. Assume time is hh:mm"
    times = time.split(":") ## ['hour', 'mins']
    degs = [hour_degree(times[0]), min_degree(times[1])]
    return(max(degs) - min(degs))


if __name__ == "__main__":
    ex = "11:30" # 11 hour is at 330 degs, 30 min is at 180 degs
    print(get_degree_from_mins(ex)) # prints 150