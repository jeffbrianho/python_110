# Write a function that takes two arguments, an inventory item ID and a 
# list of transactions, and returns a list containing only the transactions 
# for the specified inventory item.

"""
I item ID (value) and list of transactions (nested dict)
O list
e only the transactions listed for that inventory

accessing a dictionary
A: 
iterate through list for dict in transactions
use key access so that if transactions['id'] is == id value we return that dict
return the index of that list so may need to use enumerate


"""

def transactions_for(id, lst):
    return [lst[indx] for indx, dictionary in enumerate(lst)
     if dictionary['id'] == id]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True