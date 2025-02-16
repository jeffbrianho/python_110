# Write a function that takes a floating point number representing an angle between
#  0 and 360 degrees and returns a string representing that angle in degrees, minutes,
#  and seconds. You should use a degree symbol (°) to represent degrees, a single quote 
# (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes
#  in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree symbol:


"""
P
i float
o: string
e: will represent a degree, min and sec. 60 mins in a degree 60 s in  a min
i: only a number given. 

E: 

D: FLOATS STRINGS
A:
take a float and create string; separate from decimal
divide first decimal by 60 as int and input as min
divide any remaining decimal by 60 as second



"""

def dms(float_num):
    string_num = str(float_num)
    deg_decimal = string_num.split('.')
    
    print(deg_decimal)

    if len(deg_decimal) == 1:
        return f"{deg_decimal[0]}{DEGREE}00'00\""
    else:
        dec_minutes = float('0.' + deg_decimal[1])
        minutes = dec_minutes * 60
        string_min = str(minutes)
        deg_min = string_min.split('.')
        print(minutes)
        second = float('0.'+ deg_min[1]) * 60
        print(second)

DEGREE = "\u00B0"





# All of these examples should print True
# print(dms(30)== "30°00'00\"")
# print(dms(76.73))# == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
print(dms(93.034773))# == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")