# We want to remove certain items from a set while iterating over it, 
# but the code below throws an error. Why is that and how can we fix it?

# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)

# we are mutating the set as we iterate which is not good. maybe create a new set?

data_set = {1, 2, 3, 4, 5}

new_set = set(data_set)

for item in data_set:
    if item % 2 == 0:
        new_set.remove(item)

data_set = new_set
print(data_set)

# i was right to use a new set, comprehensions acheive this better. 

new_set = {item for item in data_set
           if item % 2 != 0}