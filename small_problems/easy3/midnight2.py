# As seen in the previous exercise, the time of day can be represented as the 
# number of minutes before or after midnight. If the number of minutes is positive, 
# the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format, and 
# return the number of minutes before and after midnight, respectively.
#  Both functions should return a value in the range 0 through 1439.

# You may not use Python's datetime module.



"""
P
I String representing time
O int in mins
E returns num in min before and after midnight
I
Q
E
D
A
after midnight use any number in hour x 60
add the remaining mins
if 1440 return 0

before midnight hour-1 x 60 and 60 - min and add the two
if 1400 return 0

"""
MINS_IN_HOUR = 60

def after_midnight(string_time):
    split_time = string_time.split(":")
    hours= int(split_time[0])
    mins = int(split_time[1])

    total_mins = (MINS_IN_HOUR * hours) + mins
    
    if total_mins != 1440:
        return total_mins
    else:
        return 0

def before_midnight(string_time):
    split_time = string_time.split(":")
    hours= int(split_time[0]) - 1
    mins = 60 - int(split_time[1])

    total_mins = (MINS_IN_HOUR * hours) + mins

    if total_mins != 1440:
        return total_mins
    else:
        return 0


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True


# Their answer
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0

    return delta_minutes