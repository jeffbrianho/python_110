# Given a dictionary, return its keys sorted by the values associated with each key.

"""

if printing my_dict iteration will return key
so for x in mydict will return key only

keysort returns values

return sorted [x for x in dict], keysort by value

"""

def order_by_value(dictionary):

    def key_sort(key):
        return dictionary[key]
    
    return sorted([key for key in dictionary], key=key_sort)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
# 1:54 mins
