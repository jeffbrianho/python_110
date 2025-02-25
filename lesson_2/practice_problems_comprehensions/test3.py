# Using the same pets dictionary, create a list comprehension that returns a list of tuples, 
# where each tuple contains the pet's name and breed for all dogs.

pets = {
    'dogs': {'Fido': {'age': 5, 'breed': 'Labrador'},
             'Rex': {'age': 3, 'breed': 'German Shepherd'}},
    'cats': {'Whiskers': {'age': 2, 'breed': 'Siamese'},
             'Mittens': {'age': 4, 'breed': 'Persian'}}
}

"""
list comprehension
list of tuples with pet name and breed

"""
#[(name, breed),(name, breed),(name, breed)]

# lst = []
# for sublist in pets.values():
#     for name, info in sublist.items():
#         animal_tup = (name, info['breed'])
#         lst.append(animal_tup)
# print(lst)

lst = [(name, info['breed']) for sublist in pets.values()
       for name, info in sublist.items()]

print(lst)