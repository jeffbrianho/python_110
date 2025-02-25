# Given the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Use a nested comprehension to create a new dictionary where the keys are the names from the original dictionary, and the values are the ages of the male family members multiplied by 2. Skip any female family members.
# The result should look something like this:

{'Herman': 64, 'Grandpa': 804, 'Eddie': 20}

"""
P
I: NESTED DICT
O: NEW DICT
E: keys names o dict. ages male x2 no female
I
E
D:diction
a:
access dictionary:
empty dict
get value of key/value pair - nest dictionary
select by'gender' == 'male'
key reassignment  = age x2 
return new dictionary

create function that will select male and x2 age
"""
#easier to grab the item and multiply it


   
# for subdict in munsters.values():
#     print((subdict))
    

    # dict_example['name'] = 'Jeff'

# alter_dict(munsters)

new_dict = {key: (value['age'] * 2) for key, value in munsters.items() if value['gender'] == 'male'}
        
print(new_dict)