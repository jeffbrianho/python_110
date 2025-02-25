# Given the following data structure, write some code to return a list that contains the colors of the 
# fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

final_list = []
for item, desc in dict1.items():
    if desc['type'] == 'fruit':
        sublist = [fruit.capitalize() for fruit in desc['colors']]
        final_list.append(sublist)
    else:
        final_list.append(desc['size'].upper())
print(final_list)



# for food in dict1:
#     if dict1[food]['type'] == 'fruit':
#         print(dict1[food]['colors'])
#     if dict1[food]['type'] == 'vegetable':
#         print(dict1[food]['size'])



# def food_type(subdict):
#     food_list = []

#     if subdict['type'] == 'fruit':
#         for color in subdict['colors']:
#             food_list.append(color.capitalize())
       
#     else:
#         food_list.append(subdict['size'].upper())
    
#     return food_list 


# new_list = [food_type(dict1[subdict]) for subdict in dict1]

# print(new_list)

# #Their answer
# def transform_item(item):
#     if item['type'] == 'fruit':
#         return [color.capitalize() for color in item['colors']]
#     else:
#         return item['size'].upper()

# result = [transform_item(item) for item in dict1.values()]
# print(result)