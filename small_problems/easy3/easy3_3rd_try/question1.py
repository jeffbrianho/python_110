# The time of day can be represented as the number of minutes before or after midnight. 
# If the number of minutes is positive, the time is after midnight. 
# If the number of minutes is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the time 
# of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.

"""
MINS_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_PER_DAY = MINS_IN_HOUR * HOURS_IN_DAY # 1440
this is math:


if while num is < 0; num = add 1440

    num % 1440
    hours = num // m60
    mins == num % 60 
"""

def time_of_day(remaining_mins):
    MINS_IN_HOUR = 60
    HOURS_IN_DAY = 24
    MINUTES_PER_DAY = MINS_IN_HOUR * HOURS_IN_DAY

    while remaining_mins < 0:
        remaining_mins += MINUTES_PER_DAY

    remaining_mins =  remaining_mins % MINUTES_PER_DAY
    hours = remaining_mins // MINS_IN_HOUR
    mins = remaining_mins % MINS_IN_HOUR

    return f'{hours:02d}:{mins:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# need help with math algoritm 10 mins 