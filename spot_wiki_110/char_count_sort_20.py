# Write a function that takes a string as an argument and groups the
# number of times each character appears in the string as a dictionary
# sorted by the highest number of occurrences.

# The characters should be sorted alphabetically, and you should ignore
# spaces, special characters, and count uppercase letters as lowercase ones.
"""
P:
I: string
O: number of times the char appears sorted by occurrences
E: ignore spaces, special char, casefold
I

E
D: dictionary
A: 

create a dictionary with a count / list letter
if exists already using .get(key, dict[key + [char])
return final dict


"""

def get_char_count(word):
    final_dict = {}
    for char in set(word.casefold()):
        if char.isalnum():
            key = word.casefold().count(char)
            if final_dict.get(key):
                final_dict[key] = final_dict[key] + [char.lower()]
            else:
                final_dict[key] = [char.lower()]
        else:
            continue

    sorted_dict = sorted(final_dict.items(), reverse=True)
    sorted_final_dict = {final_key: sorted(final_value)
                         for final_key, final_value in sorted_dict}
    return sorted_final_dict

# Examples:
print(get_char_count("Mississippi") == {4: ['i', 's'], 2: ['p'], 1: ['m']})
print(get_char_count("Hello. Hello? HELLO!!") == {6: ['l'], 3: ['e', 'h', 'o']})
print(get_char_count("aaa...bb...c!") == {3: ['a'], 2: ['b'], 1: ['c']})
print(get_char_count("aaabbbccc") == {3: ['a', 'b', 'c']})
print(get_char_count("abc123") == {1: ['1', '2', '3', 'a', 'b', 'c']})