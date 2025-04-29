# Write a function that takes a lowercase string as input and returns the
# length of the longest substring that consists entirely of vowels (a, e, i, o, u).

VOWELS = 'aeiou'

def create_substrings(s):
    return [s[start:end] for start in range(len(s)) 
            for end in range(start + 1, len(s) + 1)]



def solve(s):
    all_substrings = create_substrings(s)
    vowel_substrings = [len(substring) for substring in all_substrings
                        if all(char in VOWELS for char in substring)]
    return max(vowel_substrings)

print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3