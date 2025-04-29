# Write a function that splits the string into pairs of two characters.
# If the string contains an odd number of characters, replace the missing second 
# character of the final pair with an underscore ('_').

def solution(string):
    if string:
        if len(string) % 2 == 0:
            return [string[indx:indx + 2] for indx in range(0, len(string), 2)]
        else:
            new_string = string + '_'
            return [new_string[indx:indx + 2] for indx in range(0, len(new_string), 2)]
    return []

print(solution('abc') == ['ab', 'c_'])
print(solution('abcdef') == ['ab', 'cd', 'ef'])
print(solution("abcdef") == ["ab", "cd", "ef"])
print(solution("abcdefg") == ["ab", "cd", "ef", "g_"])
print(solution("") == [])