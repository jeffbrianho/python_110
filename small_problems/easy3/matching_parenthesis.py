# Write a function that takes a string as an argument and returns True 
# if all parentheses in the string are properly balanced, False otherwise. 
# To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

"""
P
I string
O Boolean
E all parentehses in string a balanced false otherwise
I must be in () pairs

E
D
A" consider a count for a string char" if count ( == count )
return boolean

if ( == + 1 and ) == -1 
if any point count is (-) return falst

"""

def is_balanced(s):
    count = 0
    
    for char in s:
        if count >= 0:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        else:
            return False
    return count == 0 
        

print(is_balanced("What (is) this?"))#== True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True