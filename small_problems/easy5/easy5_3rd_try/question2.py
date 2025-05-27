# Given a dictionary and a list of keys, produce a new dictionary that only contains the 
# key/value pairs for the specified keys.

"""
I: DICTIONARY and list of keys
O: dictionary
E: new dic specified by key (selection based)
I

E:

iterate through input; if in key append dict
"""

def keep_keys(input, key):
    return {item: value for item, value in input.items()
            if item in key}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# without both the output would be a set not dict

