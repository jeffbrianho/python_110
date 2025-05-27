# Given a dictionary where both keys and values are unique, 
# invert this dictionary so that its keys become values and its values become keys.

"""
P
I: DICTIONARY
O: DICTIONARY
E: INVERT Values/keys
Iall strings

E
D: dict

A: comprehension dict for key value return value key

"""

def invert_dict(dictionary):
    return {group: example
            for example, group in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# 2:34 mins did pedac and returned 1st try