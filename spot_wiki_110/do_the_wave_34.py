# Create a function that turns a string into a Wave. You will be passed a string
# and you must return that string in an array where an uppercase letter is a person standing up.

"""
A:
iterate through string index, if_isalpha:
    replace string index , char.upper
    send to list
return list
"""

def wave(string):
    final_list = []

    char_list = list(string)
    
    for idx, char in enumerate(char_list):
        if char.isalpha():
            mod_list = char_list[:]
            mod_list[idx] = char.upper()
            final_list.append(''.join(mod_list))
    
    return final_list
        

print(wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
print(wave("") == [])
print(wave("two words")== ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])