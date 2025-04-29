# Write a function that takes a non-empty string `s` as input and finds the
# minimum substring `t` and the maximum number `k`, such that the entire string
# `s` is equal to `t` repeated `k` times.

# Examples:

def create_substring(string):
    return [string[start:end] for start in range(len(string))
            for end in range(start + 1, len(string) + 1)]

def f(string):
    lst_of_substrings = list(set(create_substring(string)))
    viable_substrings = []

    for substring in lst_of_substrings:
        for k in range(len(string)):
            if substring * k == string:
                viable_substrings.append([substring, k])

    def string_length(sublist): ## this section required a lambda but think of making a key like sort
        return len(sublist[0])

    final_sublist = min(viable_substrings, key=string_length) # created key stringlength of [0] providing the min 
    return final_sublist

# 

print(f("ababab") ==["ab", 3])