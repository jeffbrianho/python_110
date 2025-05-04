from string_to_number import string_to_integer


def string_to_signed_integer(s):
    if '-' in s:
        return (-1 * string_to_integer(s[1:]))
    elif '+' in s:
        return string_to_integer(s[1:])
    else:
        return string_to_integer(s)




#Their answer

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

def string_to_integer(string):
    NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    number_total = 0 

    for idx, char in enumerate(string):
        number_total += NUM_LIST.index(char) * (10 ** (len(string) - (idx + 1)))


    return number_total

def string_to_signed_integer(string):

    if string[0].isdigit():
        return string_to_integer(string)
    elif string[0] == '-': 
        return string_to_integer(string[1:]) * -1
    else:
        return string_to_integer(string[1:])
    


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# for both function ~ 14 mins
