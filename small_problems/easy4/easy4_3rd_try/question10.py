# Building on the previous exercise, write a function that returns True or False 
# based on whether or not an inventory item (an ID number) is available. As before,
#  the function takes two arguments: an item ID and a list of transactions. 
# The function should return True only if the sum of the quantity values of the item's 
# transactions is greater than zero. Notice that there is a movement property in each transaction object. 
# A movement value of 'out' will decrease the item's quantity.

# You may (and should) use the transactions_for function from the previous exercise.


"""
I: id and list of transactions
O: boolean
e: sum of quantitiy is > 0 out = subtract in means add

obtain list of needed item

create a functino to get sum of quantity
set count = 0 
iterate trhough items
if movement in += count the quantity
if out -= count the quantity
dictionar[movement] - dictionary [quant]

create functino to out if quantity is > 0 
isolate items using transactions for - will get a list of items of the wanted amount
count the items with `item_amount`
if return is >0 then return True - set to "itemamount > 0" 


"""
def transactions_for(item_id, items):
    return [inventory 
            for inventory in items
            if inventory['id'] == item_id]

def item_amount(list_of_items):
    count = 0
    for item in list_of_items:
        if item['movement'] == 'in':
            count += item['quantity']
        elif item['movement'] == 'out':
            count -= item['quantity']
    
    return count

def is_item_available(item_id, items):
    return item_amount(transactions_for(item_id, items)) > 0


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

# did a good job using PEDAC 8:31 mins
