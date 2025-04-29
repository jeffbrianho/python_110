# Write a function triple_double(num1, num2) which takes numbers num1 and num2
# and returns 1 if there is a straight triple of a number at any place in num1
# and also a straight double of the same number in num2. If this isn't the case,
# return 0
"""
P
I: two numbers
O: integer (1, 0)
E: if first num is a triple at any point and if second is a double at any point
I: only numbers

E: must be trip/doub to return 1 else 0 
D: lists; 
maybe dict to check for count

A:
high level:
check if there is a recurring number 3x in the num and provide True/False
check if there is a recurring number 2x in num2 and provide True/False
if both conditions True return 1 else 0

consider slicing through the number and see if the individual num is the same broken up
for num 1 slice x3 [0:3] and iterate up 1:4 etc
each slice if list(str(num)) to provide 666 => [6, 6, 6] if ele == ele2 == ele3 return True can break statment
same for num 2 for slice x2 consider comprehension. 

if both True - return 1 else 0 

"""

def triple_double(num1, num2):
    str_num1 = str(num1)
    sliced_num1 = [str_num1[start:start + 3] for start in range(len(str_num1))
                   if len(str_num1[start:start + 3]) == 3 ]

    seperated_num_list1 = [list(num) for num in sliced_num1]
    
    is_triple_list = []
    is_double_list = []

    for num_lst1 in seperated_num_list1:
        a, b, c = num_lst1
        is_triple_list.append(a == b == c)

    str_num2 = str(num2)
    sliced_num2 = [str_num2[start:start + 2] for start in range(len(str_num2))
                   if len(str_num2[start:start + 2]) == 2 ]

    seperated_num_list2 = [list(num) for num in sliced_num2]

    for num_lst2 in seperated_num_list2:
        a, b = num_lst2
        is_double_list.append(a == b)

    if all((any(is_triple_list), any(is_double_list))):
        return 1
    
    return 0 
    
    

        


print(triple_double(12345, 12345)== 0)
print(triple_double(666789, 12345667) == 1) # 3 straight 6's in num1, 2 straight 6's in num2

# Time to complete = 25:27 mins
# Theme: checking consecutive integers for condition
# Approach: slice and check if triple by using unpacking assignment to check for equality
# conditionals