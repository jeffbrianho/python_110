# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the 
# opportunity to go for a short walk. The city provides its citizens with a Walk Generating App 
# on their phones -- every time you press the button it sends you a list of one-letter strings
#  representing directions to walk (e.g., ['n', 's', 'w', 'e']). You always walk only a single
#  block in a direction, and you know it takes you one minute to traverse one city block. 
# Create a function that will return `True` if the walk the app gives you will take you exactly
#  ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.
#  Return `False` otherwise.

# Note: You will always receive a valid list containing a random assortment of direction letters 
# ('n', 's', 'e', or 'w' only). It will never give you an empty list (that's not a walk, that's standing still!).

"""
algo:
must be 10 mins
easy check 10 directions long 
n can be +1 s can be -1 and must sum to 0 e and w can be +2 and -2
if sum of all letter does not equal 0, return false


use function to convert all letters to numbers
sum the numbers
"""

def make_direction_to_num(lst_of_letters):
    final_list = []
    for direction in lst_of_letters:
        match direction:
            case 'n':
                final_list.append(1)
            case 's':
                final_list.append(-1)
            case 'e':
                final_list.append(2)
            case 'w':
                final_list.append(-2)
    return final_list

def is_valid_walk(lst_of_directions):
    if len(lst_of_directions) != 10:
        return False
    elif sum(make_direction_to_num(lst_of_directions)) != 0:
        return False
    else:
        return True



# Examples:
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True)
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])  == False)
print(is_valid_walk(['w']) == False)
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])  == False)