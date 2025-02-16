from string_to_number import string_to_integer


def string_to_signed_integer(s):
    if '-' in s:
        return (-1 * string_to_integer(s[1:]))
    elif '+' in s:
        return string_to_integer(s[1:])
    else:
        return string_to_integer(s)



print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True