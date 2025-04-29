# Write a function named join_or that produces the following results:

def join_or(lst, sep=', ', end='or'):
    final_string = ''
    
    for indx, num in enumerate(lst):
        if len(lst) == 1:
            final_string += str(num)
        elif len(lst) > 2 and indx != (len(lst) - 1):
            final_string += str(num) + sep
        elif len(lst) == 2 and indx != (len(lst) - 1):
            final_string += str(num) + ' '
        else:
            final_string += end + ' ' + str(num)
    return final_string



# Their answer:
# def join_or(sequence, delimiter=', ', word='or'):
#     match len(sequence):
#         case 0:
#             return ''
#         case 1:
#             return str(sequence[0])
#         case 2:
#             return f"{sequence[0]} {word} {sequence[1]}"

#     leading_items = delimiter.join(str(item) for item in sequence[0:-1])
#     return f'{leading_items}{delimiter}{word} {sequence[-1]}'


print(join_or([1, 2, 3])               == "1, 2, or 3")
print(join_or([1, 2, 3], '; ')         == "1; 2; or 3")
print(join_or([1, 2, 3], ', ', 'and')  == "1, 2, and 3")
print(join_or([])                      == "")
print(join_or([5])                     == "5")
print(join_or([1, 2])                  == "1 or 2")