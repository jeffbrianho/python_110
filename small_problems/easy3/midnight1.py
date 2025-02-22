# The time of day can be represented as the number of minutes before or after midnight. 
# If the number of minutes is positive, the time is after midnight. If the number of minutes 
# is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the time 
# of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.


"""
P
I INT positive or negative
O string of (hh':mm") timeframe

E: negative is subtracted from 2400
I

E
D
A:
this is math =(
go by 60 intervals if num is abs > 60 then divide by 60 for hours and mins
if not sub or add pending pos or negative
if pos start at 0 if neg start at 24:00

"""

def time_of_day(num):
    if abs(num) > 1440:
        over_day_time = abs(num) / 60
        while over_day_time > 24:
            over_day_time -= 24
        if num < 0:
            print(f'{24 - over_day_time}')
    
    if abs(num) > 60:
        greater_than_hour = num / 60

        if greater_than_hour > 24:
            greater_than_day = greater_than_hour / 24




# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800))# == "13:20")      # True
print(time_of_day(-4231))# == "01:29")    # True