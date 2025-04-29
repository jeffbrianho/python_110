# Sort the given strings in alphabetical order, case insensitive.

"""
sort in alpha?
easy sort with key.lower()?
"""

def sortme(list_of_strings):
    return (sorted(list_of_strings, key=str.lower))

print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])

# 1.49 min 