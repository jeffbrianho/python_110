# Write a function `scramble(str1, str2)` that returns `True` if a portion of
# `str1` characters can be rearranged to match `str2`, otherwise returns `False`.

# Notes:
# - Only lower case letters will be used (a-z). No punctuation or digits will
# 	be included.
# - Performance needs to be considered.
# - Input strings `str1` and `str2` are null terminated.




def scramble(str1, str2):
    return all([char in str1 for char in str2])

# Examples:

print(scramble('rkqodlw', 'world') == True)
print(scramble('cedewaraarossoqqyt', 'carrot') == True)
print(scramble('katas', 'steak') == False)
print(scramble('scriptjava', 'javascript') == True)
print(scramble('scriptingjava', 'javascript') == True)