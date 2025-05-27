# Finished in 6:44 mins


# Sherlock has to find suspects on his latest case. He will use your method.
# Suspect in this case is a person which has something not allowed in his/her
# pockets.
# Allowed items are defined by an array of numbers.
# Pockets contents are defined by map entries where key is a person and
# value is one or few things represented by an
# array of numbers (can be nil or empty array if empty).



pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

def find_suspects(dictionary, allowed_items):
    suspect_list =  [name for name, items in dictionary.items()
            if any([item not in allowed_items for item in items])]
    if suspect_list:
        return suspect_list
    else:
        return None
    


print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])