# Write a function that takes a string, doubles every character in the string, then 
# returns the result as a new string.



def repeater(string):
    new_string = ''

    for char in string:
        new_string += char * 2
    
    return new_string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# 42 seconds easy iteration