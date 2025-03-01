pets = {
    'dogs': {'Fido': {'age': 5, 'breed': 'Labrador'},
             'Rex': {'age': 3, 'breed': 'German Shepherd'}},
    'cats': {'Whiskers': {'age': 2, 'breed': 'Siamese'},
             'Mittens': {'age': 4, 'breed': 'Persian'}}
}

old_animals = {}

for key, dictionary in pets.items():
    for name, nest_dict in dictionary.items():
        if nest_dict['age'] > 3:
            old_animals[key] = {name: nest_dict}

print(old_animals)