# Modify the kebabize function so that it converts a camel case string into a
# kebab case. Kebab case separates words with dashes '-'; camel case identifies
# separate words by upcasing the first character in each new word.

"""
final_string = ''
loop through each char in string to find if upper()
ifupper return -char.lower() else return char
return string
"""

def kebabize(string):
    final_string = ''
    for char in string:
        if not char.isalpha():
            continue
        elif char.isupper():
            final_string += '-' + char.lower()
        else:
            final_string += char
    return final_string


# Examples:
print(kebabize('camelsHaveThreeHumps') =='camels-have-three-humps')
print(kebabize('myCamelHas3Humps') == 'my-camel-has-humps')
