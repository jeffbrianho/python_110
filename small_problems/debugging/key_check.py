# You have a function that should check whether a key exists in 
# a dictionary and returns its value. However, it's raising an error.
#  Why is that? How would you fix this code?

# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))

# key access raises an error if key not in dict so we can either
# use get method
# use conditional "in"

def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))

def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))