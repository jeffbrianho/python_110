# As seen in the previous exercise, the time of day can be represented as the number 
# of minutes before or after midnight. If the number of minutes is positive, the time is after 
# midnight. If the number of minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format, and return the number 
# of minutes before and after midnight, respectively. Both functions should return a value in 
# the range 0 through 1439.

# You may not use Python's datetime module.

"""
this is reverse math
if we do hours times mins in hours we can get mins
and then add mins for after midnight we will get total mins
get remainder to ensure 1440

for before mid night sub mins to get total:

"""

MINS_IN_HOUR = 60 
HOURS_IN_DAY = 24
MINS_IN_DAY = MINS_IN_HOUR * HOURS_IN_DAY

def after_midnight(string):
    

    hours = int(string.split(':')[0]) 
    mins = int(string.split(':')[1])

    total_mins = (hours * MINS_IN_HOUR) + mins

    total_mins = total_mins % MINS_IN_DAY

    return (total_mins)

def before_midnight(string):

    return (MINS_IN_DAY - after_midnight(string)) % MINS_IN_DAY


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True