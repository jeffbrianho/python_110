# Write a function that returns a list of all palindromic substrings of a string. 
# That is, each substring must consist of a sequence of characters that reads the same 
# forward and backward. The substrings in the returned list should be sorted by their order
#  of appearance in the input string. Duplicate substrings should be included multiple times.

# You may (and should) use the substrings function you wrote in the previous exercise.

# For the purpose of this exercise, you should consider all characters and pay attention to case; t
# hat is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single 
# characters are not palindromes.

"""
I string
O list of strings with palindromes
E in order of appearance, same forward and backwards, case matters, all mutliples printed

D functions for iterating through string
A: 
iterate through word and input each starting point, use conditional to sort if string == reverse string, append to list
return list

"""

def leading_substrings(string):
    return [string[:indx + 1] for indx in range(len(string))]

def substrings(string):
    results = []
    for indx in range(len(string)):
        starting_string = string[indx:]
        for substring in leading_substrings(starting_string):
            results.append(substring)
    return results

def palindromes(string):
    return [element for element in substrings(string) if is_palindrome(element)]

def is_palindrome(element):
    return element == element[::-1] and len(element) > 1

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

## second attempt 3 min

def all_substrings(string):
    return [string[start:end] for start in range(len(string))
                            for end in range(start + 1, len(string) + 1)]

def palindromes(string):
    return [substring for substring in all_substrings(string)
            if substring == substring[::-1]
            if len(substring) > 1]