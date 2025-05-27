# Create a function that takes a string argument and returns a dict object in which the 
# keys represent the lowercase letters in the string, and the values represent how often the 
# corresponding letter occurs in the string.


"""
P:
I: string
O: dict
E
I


E
D
A

"""

def count_letters(s):
    return {char: s.count(char)
            for char in s
            if char.islower()}


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})


# made some stupid mistakes cause I rushed the pedac and didnt understand the problem 4:42 mins
