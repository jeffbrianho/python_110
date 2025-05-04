# Write a function that takes a dictionary and a threshold value, and returns a new dictionary 
# containing only key-value pairs where the value is greater than the threshold.

"""
i dictionary, threshhold int
o dictionary
E: key value pairs where value is > threshold
"""

def filter_dictionary_by_threshold(dictionary, threshold):
    return {key: value for key, value in dictionary.items()
                                if value > threshold}

# Example:
# print(filter_dictionary_by_threshold({"a": 10, "b": 5, "c": 15, "d": 3}, 7))  # Output: {"a": 10, "c": 15}
# print(filter_dictionary_by_threshold({"apple": 8, "banana": 12, "cherry": 6}, 10)) # Output: {"banana": 12}
# print(filter_dictionary_by_threshold({"x": 1, "y": 2, "z": 3}, 5))  # Output: {}

#2

# Write a function that counts the number of vowels in a string,
#  but stops counting immediately if it encounters the character 'x'.

def count_vowels_until_x(string):
    VOWELS = 'aeiou'
    count = 0

    for char in string:
        if char in VOWELS:
            count += 1
        elif char == 'x':
            break
        else:
            continue

    return count
# Example:
# print(count_vowels_until_x("hello world"))     # Output: 3
# print(count_vowels_until_x("aeioux hello"))    # Output: 4
# print(count_vowels_until_x("xyz"))             # Output: 0

# 3
# Write a function that processes a list of numbers, skipping any negative numbers, 
# doubling any even numbers, and tripling any odd positive numbers.


def process_numbers(numbers):
    result = []
    for num in numbers:
        if num < 0:
            continue
        elif num % 2 == 0:
            result.append(num * 2)
        else:
            result.append(num * 3)
    return result

# Example:
# print(process_numbers([1, -2, 3, 4, -5, 6]))   # Output: [3, 8, 18]
# print(process_numbers([2, 5, -1, 7]))          # Output: [4, 15, 21]

# Write a function that searches a dictionary for a specific key pattern 
# (containing a certain substring) and returns the first matching key-value pair.
#  If no match is found, return None.

def find_key_with_pattern(dictionary, pattern):
    for key in dictionary:
        if pattern in key:
            return (key, dictionary[key])
# Example:
# print(find_key_with_pattern({"apple_1": 5, "banana_2": 10, "cherry_3": 15}, "ana"))  # Output: ("banana_2", 10)
# print(find_key_with_pattern({"user_id": 42, "admin_id": 1, "guest_num": 100}, "id"))  # Output: ("user_id", 42)
# print(find_key_with_pattern({"abc": 1, "def": 2}, "xyz"))  # Output: None

# 5

# Write a function that counts words in a string, but skips counting any word that starts with a
#  special character (like '@', '#', '$').

def count_normal_words(text):
    word_text = text.split()
    count = 0

    for word in word_text:
        if word[0].isalnum():
            count += 1
        else:
            continue
    return count

# Example:
# print(count_normal_words("hello world @username #hashtag normal"))  # Output: 3
# print(count_normal_words("no special characters here"))  # Output: 4
# print(count_normal_words("@all #everything $money"))  # Output: 0


# 6

# Write a function that iterates through a nested list and returns the first prime number found.
#  If no prime number exists, return -1.

def find_first_prime(nested_list):
    
    def is_prime(num):
        if num < 2:
            return False
        
        return all([num % div for div in range(2, num)])
    
    for sub_list in nested_list:
        for element in sub_list:
            if is_prime(element):
                return element
            else:
                continue
    return -1 

# Example:
# print(find_first_prime([[4, 6], [8, 9], [7, 10]]))  # Output: 7
# print(find_first_prime([[4, 6], [8, 10], [12, 15]]))  # Output: -1
# print(find_first_prime([[11], [4, 6], [8, 9]]))  # Output: 11



# 7

# Write a function that iterates through a dictionary and computes a running sum of values, 
# but stops if the sum exceeds a certain threshold and returns that partial sum.

def sum_until_threshold(dictionary, threshold):
    running_sum = 0
    final_sum = 0

    
    for value in dictionary.values():
        running_sum += value
        if running_sum < threshold:
            final_sum = running_sum

    return final_sum
        
# Example:
# print(sum_until_threshold({"a": 5, "b": 10, "c": 15, "d": 20}, 30))  # Output: 30
# print(sum_until_threshold({"a": 5, "b": 10, "c": 15, "d": 20}, 50) ) # Output: 50
# print(sum_until_threshold({"a": 100}, 50))  # Output: 0

# 8
# Write a function that removes every other element from a list without using list slicing.

def remove_every_other(lst):
    return [ele for indx, ele in enumerate(lst)
                    if indx % 2 == 0]

# Example:
# print(remove_every_other([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
# print(remove_every_other(['a', 'b', 'c', 'd'])) # Output: ['a', 'c']
# print(remove_every_other([10]) ) # Output: [10]


# 9

# Write a function that searches a string for a pattern. Once found, 
# continue searching for the next occurrence but skip the next 3 characters after each match.

def find_pattern_with_skip(text, pattern):
    output = []
    indx = 0

    while indx < len(text):
        if pattern in text[indx: indx + len(pattern) + 1]:
            output.append(text.index(pattern, indx))
            indx += 3
        else:
            indx += 1

    return output



# Example:
# print(find_pattern_with_skip("ababababa", "ab"))  # Output: [0, 4, 8]
# print(find_pattern_with_skip("aaaaa", "aa") ) # Output: [0, 3]
# print(find_pattern_with_skip("hello world", "l"))  # Output: [2, 6, 9]

# 10

# Write a function that takes a list of numbers and performs these operations in sequence:
# 1.  Skip the first two elements
# 2.  Process the next three elements
# 3.  Skip two more elements
# 4.  Process all remaining elements
# Return a list of all processed elements that are prime numbers.

def process_with_custom_rules(numbers):
    INDICES = {0, 1, 5, 6}

    def is_prime(num):
        if num < 2:
            return False
        else:
            return all([num % div != 0 for div in range(2, num)])
    
    return [num for indx, num in enumerate(numbers)
            if is_prime(num)
            if indx not in INDICES
            ]

# Example:
print(process_with_custom_rules([1, 4, 3, 5, 7, 8, 9, 11, 13, 15]))  # Output: [3, 5, 7, 11, 13]
print(process_with_custom_rules([4, 6, 8, 9, 10, 12, 13, 17, 20]))  # Output: [13, 17]

# 1

def filter_dictionary_by_threshold(dictionary, threshold):
    return {key: value for key, value in dictionary.items()
                                if value > threshold}


# 2

def count_vowels_until_x(string):
    VOWELS = 'aeiou'
    count = 0

    for char in string:
        if char in VOWELS:
            count += 1
        elif char == 'x':
            break
        else:
            continue

    return count



# 3

def process_numbers(numbers):
    result = []
    for num in numbers:
        if num < 0:
            continue
        elif num % 2 == 0:
            result.append(num * 2)
        else:
            result.append(num * 3)
    return result


# 4

def find_key_with_pattern(dictionary, pattern):
    for key in dictionary:
        if pattern in key:
            return (key, dictionary[key])


# 5

def count_normal_words(text):
    word_text = text.split()
    count = 0

    for word in word_text:
        if word[0].isalnum():
            count += 1
        else:
            continue
    return count

# 6
def find_first_prime(nested_list):
    
    def is_prime(num):
        if num < 2:
            return False
        
        return all([num % div for div in range(2, num)])
    
    for sub_list in nested_list:
        for element in sub_list:
            if is_prime(element):
                return element
            else:
                continue
    return -1 

# 7 

def sum_until_threshold(dictionary, threshold):
    running_sum = 0
    final_sum = 0

    
    for value in dictionary.values():
        running_sum += value
        if running_sum < threshold:
            final_sum = running_sum

    return final_sum

# 8 

def remove_every_other(lst):
    return [ele for indx, ele in enumerate(lst)
                    if indx % 2 == 0]

# 9 

def find_pattern_with_skip(text, pattern):
    output = []
    indx = 0

    while indx < len(text):
        if pattern in text[indx: indx + len(pattern) + 1]:
            output.append(text.index(pattern, indx))
            indx += 3
        else:
            indx += 1

    return output

# 10
def process_with_custom_rules(numbers):
    INDICES = {0, 1, 5, 6}
    
    def is_prime(num):
        if num < 2:
            return False
        else:
            return all([num % div != 0 for div in range(2, num)])
    
    return [num for indx, num in enumerate(numbers)
            if is_prime(num)
            if indx not in INDICES
            ]



# corrections

def sum_until_threshold(dictionary, threshold):
    running_sum = 0
    
    for value in dictionary.values():
        if running_sum + value > threshold:
            break
        running_sum += value
    
    return running_sum

def find_pattern_with_skip(text, pattern):
    output = []
    indx = 0

    while indx < len(text):
        found_at = text.find(pattern, indx)
        if found_at != -1:
            output.append(found_at)
            indx = found_at + len(pattern) + 3  # Skip 3 characters after the pattern
        else:
            break  # No more patterns found
    
    return output