# One of the most frequently used real-world string operations is that of "string substitution,"
#  where we take a hard-coded string and modify it with various parameters from our program.

# Given the object shown below, print the name, age, and gender of each family member:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for person in munsters:
#     print(f'{person} is a {munsters[person]['age']}-year-old {munsters[person]['gender']}')

# Their Answer
for name, info in munsters.items():
    # print(f"{name} is a {info['age']}-year-old {info['gender']}.")
    print(info)
#break into key value pairs where key is name and info is dictionary of age/gender then use the info as 
# the dict to unpack; info is the dict!


# (name) is a (age)-year-old (male or female).

# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.