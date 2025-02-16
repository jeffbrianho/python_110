# PEDAC GUIDED PRACTICE: Sort by Most Adjacent Consonants
"""
Step 1: Understand the Problem
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the 
highest number of adjacent consonants a string contains
and return the sorted list. If two strings contain the 
same highest number of adjacent consonants, they should 
retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to 
each other in the same word or if there is a space between
two consonants in adjacent words.

Tasks

You are provided with the problem description above.
 Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.

INPUT: List of strings
OUTPUT: list of strings sorted
EXPLICIT: sort based off highest number of adjacent consonants
adjacent is next to each other or separated by a space in words
keep same order if same number
IMPLICIT: non-adjacent means a vowel separates it and starts the count again


does caps matter
are there any non alpha words?

NOTES:
INPUT AND OUTPUTS
- Input: list of strings
- Output: a list of strings sorted according to the highest number
  of adjacent consonants

EXPLICIT:
- If two strings contain the same highest number of adjacent
  consonants, they should maintain their original relative order.
- Adjacent consonants:
    - are next to each other in the same string.
    - can have a space between them in adjacent
      words.

IMPLICIT
Strings may contain more than one words.

QUESTIONS
- Do strings always contain multiple words?
    - Can strings contain a single word?
    - Can strings be empty?
- Is it possible for a string to contain no adjacent consonants?
- What is meant by "a space between two consonants in adjacent
  words"?
- Should the strings be sorted in ascending or descending order?
- Is case important?


Step 2: Exampees and test cases

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

it counts the adjacent consonants not the amount of consonants so aa is == baa as their are no adjacent consonants

QUESTIONS
- Do strings always contain multiple words? [No]
    - Can strings contain a single word? [Yes]
    - Can strings be empty? [No]
- Is it possible for a string to contain no adjacent consonants?
  [Yes]
- What is meant by "a space between two consonants in adjacent
  words"? [A consonant that ends one word followed by a consonant
  that starts a new word are adjacent.]
- Should the strings be sorted in ascending or descending order?
  [Descending]
- Is case important? [No]

IMPLICIT RULES
- Strings may contain single or multiple words.
- Strings may not be empty.
- Strings may have no adjacent consonants.
- Strings should be sorted in descending order.
- Case is not relevant.

- Strings may contain single or multiple words.
- Strings may not be empty.
- Strings may have no adjacent consonants.
- Strings should be sorted in descending order.
- Case is not relevant.
- Single consonants in a string do not affect sort order in
  comparison to strings with no consonants. Only adjacent
  consonants affect sort order.

STEP 3: Data Structures
may use a dictionary to sort the number of adjacent consonants

{
    'aa': 0,
    'baa': 0,
    'ccaa': 2,
    'dddaa': 3,
    'rstafgdjecc': 4,
}

Step 4: Algorithm

1. Assess each string in the list
2. Count through each character and address each consecutive consonant
3. Store each string and its associated count
4. Sort the amount based off the count
5. return the strings as a list in new order

the count needs more work
ANSWER:
Dive deep into the count
its repeated so a loop is needed

THINK INPUT OUT
Input: a string
Output: an integer representing a count of the highest number of
        adjacent consonants in the string

TEST CASES
print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4

We need to manipulate the input string to remove any spaces.
We don't want to update the count if the temporary string contains only one consonant.

- Remove the spaces from the "input string".
- Initialize a "maximum consonants count" to zero.
- Initialize an "adjacent consonants string" to an empty string.
- For each "letter" in the "input string":
    - If the "letter" is a consonant:
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".

CODE:
"""

def count_max_adjacent_consonants(s):
    no_space_string = ''.join(s.split(' '))

    max_count = 0
    adjacent_consonants = ''

    for char in no_space_string:
        if char.lower() not in {'a', 'e', 'i', 'o', 'u'}:
            adjacent_consonants += char
        else:
            if len(adjacent_consonants) > max_count:
                if len(adjacent_consonants) > 1:
                       max_count = len(adjacent_consonants)
            adjacent_consonants = ''
    return max_count

def sort_by_consonant_count(string_list):
    string_list.sort(key=count_max_adjacent_consonants, reverse=True)
 
    return string_list
          

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']