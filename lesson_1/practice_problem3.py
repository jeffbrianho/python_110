a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# c = a | b 
# print(c)

# new_set = set()
# for num in a:
#     new_set.add(num)
# for num in b:
#     new_set.add(num)

# print(new_set)

c = a.union(b)
print(c)