# Use a dictionary comprehension to create a new dictionary that contains only
#  the pets that are older than 3 years.

pets = {
    'dogs': {'Fido': {'age': 5, 'breed': 'Labrador'},
             'Rex': {'age': 3, 'breed': 'German Shepherd'}},
    'cats': {'Whiskers': {'age': 2, 'breed': 'Siamese'},
             'Mittens': {'age': 4, 'breed': 'Persian'}}
}

# new_dict = {}
# for type, animal in pets.items():
    
#     for pet, info in animal.items():
#         if info['age'] > 3:
#             new_dict[type] = {pet: info}
            


new_dict = {type: {pet:info} for type, animal in pets.items()
            for pet, info in animal.items()
            if info['age'] > 3}

print(new_dict)

{'dogs': {'Fido': {'age': 5, 'breed': 'Labrador'}}, 'cats': {'Mittens': {'age': 4, 'breed': 'Persian'}}}

# new_dict = {type: animal for type, animal in pets.items()
#             for pet, info in animal.items()
#             if info['age'] > 3}            

# print(new_dict)