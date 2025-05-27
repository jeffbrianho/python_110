# We're receiving a set of messages in code. The messages are sets of text strings, like:
# "alakwnwenvocxzZjsf"
# Write a method to decode these strings into numbers. The decoded number 
# should be the number of lowercase characters between the first two uppercase characters.
#  If there aren't two uppercase characters, the number should be 0.

def decode(lst):

    def count_lowers(word):
        indx = 0
        count = 0
        while indx < len(word):         # while loops allow me to control when to break into the count with indices
            if word[indx].islower():    # when word is lower we continue through loop
                indx += 1
               
            elif word[indx].isupper():    # if we hit an upper we start the count and enter the new loop 
                
                indx += 1               # take the next indices to ensure we count the next lower
                while indx < len(word):
                    if word[indx].islower() and indx != (len(word) - 1):    # if lower and not the last letter  
                        count +=1                                           # add to count and increase the index
                        indx += 1
                    elif word[indx].isupper():                              # if we hit the upper we break
                        break
                    else:                                                   # if we get to the end without an upper
                        count = 0                                           # reset count to 0 and break
                        break
                    
                return count                    # keeping the count in the inner if statement ensures we exit the outer while
        return count                           
    
    return [count_lowers(word) for word in lst]  
        
# Test cases:

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])




# SPEND MORE TIME ON TEST CASES
# MORE ALGORITM

# when we iterate where do we start where do we stop

# Data structures - what specifics? do we need to create 