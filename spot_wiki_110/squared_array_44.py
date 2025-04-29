# Given two arrays a and b write a function comp(a, b) that checks whether
# the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in `b` are the elements in `a` squared,
# regardless of the order.

"""
P:
I: Two arrays (lsts)
O: Boolean
E: check to see if they have the same elements with same multiplicities; elements in a squared are same in b
order doesn't matter
I: if empty or None return False

E:
D:
lists

A:
comparing whether squares of a are in b regardless of order
we can square the former and check for membership in latter
None return false and empty strings return false

square the first list (a):
iterate the first list against membership in second list (a ele in b)
if return all(True) 

"""
def return_squared_lst(lst):
    return [num**2 for num in lst]

def comp(a, b):
    if a:
        squared_a_lst = return_squared_lst(a)

    if a and b and len(a) == len(b):
        return all([num in b for num in squared_a_lst])
    
    return False

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)

# Time to complete: 11 mins
# Theme: comparison of two lsts using several conditionals
# Approach: direct conditionals and transformations