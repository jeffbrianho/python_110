# Write a function `longest(s)` that finds and returns the longest substring of
# `s` where the characters are in alphabetical order.

"""
created every substring: v
create a sorted reference and in sub == sort store in list
return max length substring

"""
def longest(string):
    all_substrings = [string[start:end] 
                                        for start in range(len(string))
                                        for end in range(start + 1, len(string) + 1)]
    
    all_sorted_substrings = [''.join(sorted(substring))
                                            for substring in all_substrings]
    
    final_sorted_substrings = [final_substring for final_substring in all_substrings
                                                if final_substring in all_sorted_substrings]
    
    longest_substring = max(final_sorted_substrings, key=len)
    return longest_substring

# Example:
print(longest('asd')                  == 'as') 
print(longest('nab')                  == 'ab')
print(longest('abcdeapbcdef')         == 'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag')        == 'fgikl')
print(longest('z')                    == 'z')
print(longest('zyba')                 == 'z')

# shelbys
# def longest(string):

#     substrings = [string[i:j] for i in range(len(string))
#                     for j in range(i + 1, len(string) + 1)]
  
#     sorted_substrings = [substring for substring in substrings if list(substring) == sorted(substring)]

#     sorted_substrings.sort(key=lambda substring: len(substring), reverse=True)

#     return sorted_substrings[0]
    
