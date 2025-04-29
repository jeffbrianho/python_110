# Lettercase Percentage Ratio

# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.
"""

P:
I: string
O: dictionary with three properties
    % of chars that are lower case
    % of chars that are upper
    $ of chars that are neither
    all three % return as strings with numerics between 0.00 and 100.00
    no empty strings
E: 5 lower
    1 cap
    1 empty space this counts
    3 nums
I

E:
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

D: strings 
dictionary with 'lower' 'upper' neither and number as values in string format 
A:

iterate through string:
use if condtions, if lower lowercoutn + 1
if upper uppercount + 1
if neither upper count + 1
 total counts and divide to get percentage. make string with e.00
 create dicts with keys accourndingly and add strings to each key


C


"""

def letter_percentages(string):
    lower_count = 0
    upper_count = 0
    neither_count = 0
    final_dict = {}

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            neither_count += 1
    total_count = (upper_count + lower_count + neither_count)
    lower_percent = (lower_count / total_count) * 100
    upper_percent = (upper_count / total_count) * 100
    neither_percent = (neither_count / total_count) * 100

    final_dict['lowercase'] = f'{lower_percent:.2f}'
    final_dict['uppercase'] = f'{upper_percent:.2f}'
    final_dict['neither'] = f'{neither_percent:.2f}'

    return final_dict

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

# Their answer

def percentage(count, total_count):
    return f'{(count / total_count) * 100:.2f}'

def letter_percentages(string):
    total_chars = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1

    return {
        'lowercase': percentage(lowercase_count, total_chars),
        'uppercase': percentage(uppercase_count, total_chars),
        'neither':   percentage(neither_count, total_chars),
    }

# they made a function for the % and hardcoded the dictionary