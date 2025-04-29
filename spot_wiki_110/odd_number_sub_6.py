# Write a function that takes a string of integers as input and returns the
# number of substrings that result in an odd number when converted to an integer.

# Examples:

def create_substrings(string):
    return [string[start:end]
            for start in range(len(string))
            for end in range(start + 1, len(string) + 1)]

def summation_of_digits(string): # I thought they wanted to summation of the number whoops!
    string_lst = list(string)
    final_sum = 0 
    for num in string_lst:
        final_sum += int(num)
    return final_sum

def is_odd(num):
    if int(num) % 2 == 0:
        return False
    return True


def solve(str_of_int):
    lst_of_substrings = create_substrings(str_of_int)

    num_of_odd_substrings = 0 

    for substring in lst_of_substrings:
        if is_odd(substring):
            num_of_odd_substrings += 1
    
    return num_of_odd_substrings
    



print(solve("1341")) # should return 7
print(solve("1357")) # should return 10