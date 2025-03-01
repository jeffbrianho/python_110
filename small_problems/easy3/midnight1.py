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

def time_of_day(mins):

    if mins >= 0:

        mins_left = mins
        count = 00

        while mins_left >= 60:
            mins_left -= 60
            if count >= 23:
                count = 0
            else:
                count += 1
        return f'{count:02d}:{mins_left:02d}'
    
    else:
        neg_mins_left = mins
        neg_count = -1
        while neg_mins_left <= -60:
            neg_mins_left += 60
            if neg_count <= -24:
                neg_count = -1
            else:
                neg_count -= 1
        
        return f'{(24 + neg_count):02d}:{(60 + neg_mins_left):02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True


#Their answer
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)