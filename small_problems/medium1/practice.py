# You are given a 0-indexed list of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# Return an array of all the palindrome pairs of words.

# You must write an algorithm with O(sum of words[i].length) runtime complexity.
"""
 I: list of unique strings
 O: list of palindrome pairs of words
 E; palindrome pair is pair of integers (int1, int2)
 int1 >= 0 and int2 < len(words)
 int1 != int2
 words[int1] + words[int2 is a palindrome]
 I

 E:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
 

 D
 
 A: iterate through all the combinations of word in words comparing index 0 + range len word to end noninclusive
use enumerate to get index and word
selection if word == word[::-1] add index to list [indx1, indx2] 
"""

def palindrome_pairs(lst): # returns all the palidrome pairs
    return [[(start), (end)]
            for start in range(len(lst))
            for end in range(len(lst))
            if (lst[start] + lst[end]) == (lst[start] + lst[end])[::-1] and
            start != end]
   

# Example 1:

# print(palindrome_pairs(["abcd","dcba","lls","s","sssll"]))# == [[0,1],[1,0],[3,2],[2,4]])
# # Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# # Example 2:

# words = ["bat","tab","cat"]
# print(palindrome_pairs(words)) # == [[0,1],[1,0]])
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

print(palindrome_pairs(["a",""]))
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]