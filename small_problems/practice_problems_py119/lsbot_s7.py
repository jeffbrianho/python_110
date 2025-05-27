# ​Intermediate​: Create a function called longest_common_prefix that takes a 
# list of strings and returns the longest common prefix string among them.

"""

P:
I: list of strings
O: returns to longest common prefix string among them 
E: all lowercase no special chars or numbers
return an empty string if nothing is in common
I

E for first one fl is common to all of them 
secod one no letter is common to all of them
third is py
empty list ==> empty string

D: 
list containing all substrings in the list
list containing the substring within all lists 

A
"""

def longest_common_prefix(string):

    def sublist_word(word):
        return [word[start:end] for start in range(len(word))
                                for end in range(start + 1, len(word) + 1)]
    
    word_sub_list = [sublist_word(word) for word in string]

    shared_set = set()

    if word_sub_list:
        for indx in range(len(word_sub_list[0])):
            if all([word_sub_list[0][indx] in word_sub_list[index] for index in range(len(word_sub_list))]):
                shared_set.add(word_sub_list[0][indx])

    if shared_set:
        return max(shared_set, key=len)
    else:
        return ""

    # Examples
print(longest_common_prefix(["flower", "flow", "flight"]) == "fl")
print(longest_common_prefix(["dog", "racecar", "car"]) == "")
print(longest_common_prefix(["python", "pypy", "py"]) == "py")
print(longest_common_prefix([]) == "")

### dont forget that you can use comprehensions to help
