# Create a function that takes two strings as arguments and returns True if some portion of the 
# characters in the first string can be rearranged to match the characters in the second. 
# Otherwise, the function should return False.

# You may assume that both string arguments only contain lowercase alphabetic characters.
#  Neither string will be empty.

"""
P:
I: strings x2
O boolean
E
I

E
D
A create list of letters, compare if all list letters in 2 are in 1
C
if char in 2 are in 1 and if count is >= in 1 compared to 2
"""

def unscramble(string1, string2):
    dict1 = {char: string1.count(char) for char in string1}
    dict2 = {char: string2.count(char) for char in string2}

    contains_all_keys = [key in dict1 
                        for key in dict2]
   
    if all(contains_all_keys):
      contains_enough_value = [dict2[key] <= dict1[key] for key in dict2]
      if all(contains_enough_value):
         return True
      else:
         return False

    else: 
      return False



print(unscramble('ansucchlohlo', 'launchschool')  == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

# 11 mins
