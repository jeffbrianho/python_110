# Sherlock has to find suspects on his latest case. He will use your method.
# Suspect in this case is a person which has something not allowed in his/her
# pockets.
# Allowed items are defined by an array of numbers.
# Pockets contents are defined by map entries where key is a person and
# value is one or few things represented by an
# array of numbers (can be nil or empty array if empty).

"""
P
I a dictionary containing people: and contents in pocket, allowable contents
O: list of names with banned contents
E: 
I: return None if nobody has, 

E: 
D: dictionary, lists, 
A: 
iterate through each persons 
iterate through each value
use boolean to see if value is in `reference_list`
if not all(). append name to final list




"""

pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

def find_suspects(dictionary_person_item, reference_list):
    final_list = []

    for person in dictionary_person_item:
        if not all(([item in reference_list for item in dictionary_person_item[person]])):
            final_list.append(person)
    
    if final_list:
        return(final_list)

    return None

print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])