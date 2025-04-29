# Write a function that takes a list of integers as input and counts the number of
# pairs in the list. A pair is defined as two equal integers separated by some
# other integer(s).

def pairs(lst_of_int):
    comparison_dict = {num: lst_of_int.count(num) for num in set(lst_of_int)}

    total_pairs = 0 
    
    for count in comparison_dict.values():
        if count % 2 == 0:
            total_pairs += count // 2

    return total_pairs

    


print(pairs([1, 2, 5, 6, 5, 2]) == 2)
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)