# In the previous exercise, you developed a function that converts non-negative numbers to strings.
#  In this exercise, you're going to extend that function by adding the ability to represent negative 
# numbers as well.

# Write a function that takes an integer and converts it to a string representation.

# You may not use any of the standard conversion functions available in Python, such as str. 
# You may, however, use integer_to_string from the previous exercise.

def break_num_list(num):
    storage_list = []
    num = abs(num)
    if num == 0:
        return [0]
    
    else:

        while num:
            storage_list.append(num % 10)
            num = num // 10

    return storage_list[::-1]

def integer_to_string(num):
    final_string = ''

    REFERENCE = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    num_list = break_num_list(num)

    for dig in num_list:
        final_string += REFERENCE[dig]
    
    return final_string

def signed_integer_to_string(number):
    
    if number > 0:
        return ('+' + integer_to_string(number))
    elif number < 0:
        return ('-' + integer_to_string(number))
    else:
        return "0"

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True