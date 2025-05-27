

def decode(lst):

    def count_lowers(word):
        indx = 0
        count = 0
        while indx < len(word):         
            if word[indx].islower(): 
                indx += 1
            
            elif word[indx].isupper():
                indx += 1          
                while indx < len(word):
                    if word[indx].islower():
                        count +=1   
                        indx += 1
                    else:
                        return count
        return 0                        
    
    return [count_lowers(word) for word in lst]  
        
# Test cases:

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])
print(decode(['abCddeeee']))


