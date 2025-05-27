# Write a function that takes two arguments, an inventory item ID and a list of transactions, 
# and returns a list containing only the transactions for the specified inventory item.

"""
I: item id(int) and list(of dicts)
O: list(of dicts)

return a new list of dicts with only the id identified

list comprehension. inputing dict with selection criteria

A iterate through transactions
create a new list and add the dictionary if id == item


"""

def transactions_for(item_id, items):
    return [inventory 
            for inventory in items
            if inventory['id'] == item_id]

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

# gets a bit tricky with nested but able to finish 1st try 3:34 mins
