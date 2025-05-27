def decode(lst):

    def count_lowers(word):
        indx = 0
        count = 0
        while indx < len(word):         # while loops allow me to control when to break into the count with indices
            if word[indx].islower():    # when word is lower we continue through loop
                indx += 1
            
            elif word[indx].isupper():   # if we hit an upper we start the count and enter the new loop 
                indx += 1                # take the next indices to ensure we count the next lower
                while indx < len(word):
                    if word[indx].islower():
                        count +=1   
                        indx += 1
                    else:
                        return count        # if we hit anything not lower return count and exit function
        return 0                            # if we get to end of string return 0     
    
    return [count_lowers(word) for word in lst]  
        
# Test cases:

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])

