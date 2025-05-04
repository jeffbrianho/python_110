# Create a function that takes a string as an argument and returns True if the string is a pangram, 
# False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least once. 
# For example, the sentence "Five quacking zephyrs jolt my wax bed." 
# is a pangram since it uses every letter at least once. Note that case is irrelevant.


"""
P
I: string
O: boolean
E: if pangram - contains every letter of the alphabet at least once. 
I

E
D
A make every letter and compare if each letter is in the string 



"""
def is_pangram(sentence):
    LETTERS = list('abcdefghijklmnopqrstuvwxyz')

    contains_letters = [letter in sentence.lower() for letter in LETTERS]
    return all(contains_letters)


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

