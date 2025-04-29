# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the input string.

"""
P
I: string
O: integer
E: it will be an integer of the number of multiple occurences
I: are no numerics only alpha

E: count the number of chars that occur more than once case insensitive:


D:
dictionary
int
strings

A:
dictionary that is caseinsensitive with char and count of chars:
create `counter X

go through dictionary for any char that occur more than onces
add 1 to a count
return the counter

"""

def duplicate_count(string):
    lowered_string = string.lower()
    dictionary_string = {char: lowered_string.count(char) 
                        for char in lowered_string}


    counter = 0
    for chars in dictionary_string:
        if dictionary_string[chars] != 1:
            counter += 1

    return counter

print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)

# 8 mins 