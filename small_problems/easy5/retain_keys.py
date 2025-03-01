# Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value 
# pairs for the specified keys.


"""
I: dict, list of keys
O: new dict with key/value pairs of specific keys
what to do if not in?
E:
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

D: dictionary, list

A:
create final dict
use list keys to obtain dictionary values
save keys and values to final dict
return final dict

"""

def keep_keys(input_dict, keys):
    final_dict = {key: input_dict[key] 
                  for key in keys
                  if key in input_dict} # ensures no KeyError

    return final_dict

    

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

