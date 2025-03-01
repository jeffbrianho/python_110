# Given a dictionary, return its keys sorted by the values associated with each key.

def obtain_key(key):
    return key[1]

def order_by_value(dictionary):
    ordered_tuple = sorted(dictionary.items(), key=obtain_key)

    return [key for key, value in ordered_tuple]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']


print(order_by_value(my_dict) == keys)  # True

# skill of using a key to access the value when creating a tuple with items dictionary(items)
# will create 'p': 8 but the obtain_key function will create 8, 'p'. it will then organize and return the sorted pair.
# the list comprehension will return a list of the key as written (line 9)
