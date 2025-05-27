# Write a function that takes a floating point number representing an angle between 0 and 
# 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. 
# You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, 
# and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree symbol:

"""
"dont forget on f-strings {:02d}"
how do we get the remainder %? % 1

make a constant of 60 mins in a degree
and 60 seconds in a min

A:
divmod num by 1 to get degree and min
multiply remainder min by 60 to get min
multiply that remainder by 60 to get second

return f string using :02f

"""

def dms(num):
    MINUTES_PER_DEGREE = 60
    SECONDS_PER_MINUTE = 60

    degree, min_remainder = divmod(num, 1)
    min_remainder = min_remainder * MINUTES_PER_DEGREE
    minutes, sec_remainder = divmod(min_remainder, 1)
    sec_remainder = sec_remainder * SECONDS_PER_MINUTE
    seconds, _ = divmod(sec_remainder, 1)

    return f'{int(degree):01d}{DEGREE }{int(minutes):02d}\'{int(seconds):02d}"'


DEGREE = "\u00B0"

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# 14:24 Took time to work out the math but able to take the divmod method from previous example
# did well 