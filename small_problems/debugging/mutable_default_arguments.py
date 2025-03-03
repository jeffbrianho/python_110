# We want to create a function that appends a given value to a list. 
# However, the function seems to be behaving unexpectedly:

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    
    lst.append(value)

    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

#when using a default lst. if it was used before, it will save it as the previous lst 
# better to just have an empty lst in the body with a conditional to use if they do not provide one