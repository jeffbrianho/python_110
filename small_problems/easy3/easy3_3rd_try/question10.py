# Write a function that takes a string as an argument and returns True if all parentheses in the 
# string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in 
# matching '(' and ')' pairs.


"""
P
I: string
O: boolean
E: all parentheses are matched an balanced
I: must start with ( and end with )
iterate through string. if enouters ( plus 1 if ) minus 1
if ever meets ) with 0 or less then return false
if count doesnt == 0 at end return false


E: must start with the ( and end ) and must match


D: count to maintain equality

A:

set count to 0
iterate through string
if char == '(' 
    - count is incremented
if char == ) and count <= 0
    - return False
elif char == )
    count is decrimented

exit loop
if count != 0 return False else return True


"""

def is_balanced(string):
    count = 0

    for char in string:
        if char == '(':
            count += 1
        elif char == ')' and count <= 0:
            return False
        elif char == ')':
            count -= 1
    
    if count != 0:
        return False
    else:
        return True

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# worked through PEDAC 7:13s
