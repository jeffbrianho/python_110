# string: index 0 - number -2
# 
lst = []
string = 'abcde'
for start in range(len(string)): # 0 , 1, 2, 3, 4
    for end in range(start + 1, len(string) + 1): # (1, 2, 3, 4, 5), (6)
        lst.append(string[start:end])


final_lst = [word for word in lst
             if word == word[::-1]]   
print(lst)
print(final_lst)    
# for word in final_list:
#    if word == word [::-1]:
#       lst.append(word)

