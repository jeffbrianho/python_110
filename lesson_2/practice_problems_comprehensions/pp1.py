# Compute and display the total age of the family's male members. 
# Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_male_age = 0
for _, description in munsters.items():
    if description['gender'] == 'male':
        total_male_age += description['age']

print(total_male_age)

total_age = sum([(description['age']) for _, description in munsters.items()
             if description['gender'] == 'male'])
print(total_age)
# The result should be 444.