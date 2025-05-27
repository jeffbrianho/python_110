# Building on the previous exercise, write a function that returns True or 
# False based on whether or not an inventory item (an ID number) is available. 
# As before, the function takes two arguments: an item ID and a list of transactions. 
# The function should return True only if the sum of the quantity values of the item's 
# transactions is greater than zero. Notice that there is a movement property in each 
# transaction object. A movement value of 'out' will decrease the item's quantity.

# You may (and should) use the transactions_for function from the previous exercise.
"""
I id number and transactions
o boolean true or false
e if in acts as positive out acts as negative if number is (+) return true false otherwise
i all numbers are positive

access the dictionaries for the id using function

use functon here
access the state of quantity using key access ["movement]
if "in" return "quantity"
else return (-1 * quantity)

put in list? and sum the final result

is item available if sum is >=0 return true
false otherwise


"""

def transactions_for(id, lst):
    return [lst[indx] for indx, dictionary in enumerate(lst)
     if dictionary['id'] == id]

def quantity_check(lst_of_dicts):

    lst_of_quantity = []

    for dictionary in lst_of_dicts:
        if dictionary["movement"] == "in":
            lst_of_quantity.append(dictionary["quantity"])
        else:
            lst_of_quantity.append(dictionary["quantity"] * -1)

    return sum(lst_of_quantity)

def is_item_available(id, lst):

    final_sum = quantity_check(transactions_for(id, lst))
    if final_sum >= 0:
        return True
    else: 
        return False


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]


print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True


#Their answer 

# def is_item_available(item, transactions):
#     relevant_transactions = transactions_for(item, transactions)
#     quantity = 0

#     for transaction in relevant_transactions:
#         if transaction["movement"] == 'in':
#             quantity += transaction["quantity"]
#         else:
#             quantity -= transaction["quantity"]

#     return quantity > 0

### second attempt 8:39

def transactions_for(id, list_of_dicts):                    # Isolates specific dictionaries
    return [dictionary for dictionary in list_of_dicts
                        if dictionary['id'] == id]


def sum_of_items(list_of_dicts):                            # will sum the quantity of items in dictionaries
    return sum([
            dictionary['quantity'] 
            if dictionary['movement'] == 'in' else (-dictionary['quantity']) 
            for dictionary in list_of_dicts
                    ])

def is_item_available(id, list_of_dicts):                   # returns if an item is in stock '> 0'
    return sum_of_items(transactions_for(id, list_of_dicts)) > 0