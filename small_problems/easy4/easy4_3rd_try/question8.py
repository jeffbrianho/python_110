# Write a function that returns a list of all palindromic substrings of a string. 
# That is, each substring must consist of a sequence of characters that reads the same 
# forward and backward. The substrings in the returned list should be sorted by their order 
# of appearance in the input string. Duplicate substrings should be included multiple times.

# You may (and should) use the substrings function you wrote in the previous exercise.

# For the purpose of this exercise, you should consider all characters and pay attention to 
# case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, 
# assume that single characters are not palindromes.


"""

I: string
O: list of all palindromic substrings
E: sequence that reads forwards and backwards
return by order of appearance dups should be included
case matters

e:

A: create all substrings with condition if substring == substring [::-1]



"""

def create_substrings(string):
    return [string[start:end] for start in range(len(string))
                            for end in range(start + 1, len(string) + 1)]

def palindromes(string):
    return [substring for substring in create_substrings(string)
                    if substring == substring[::-1] and len(substring) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

# 2:39 mins needed to consider char length as len 1 was showing up
