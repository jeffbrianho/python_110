# A developer is trying to remove duplicates from a list. 
# They use a set for deduplication, but the order of elements is lost.
#  How can we preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))

# print(unique_data)# == [4, 2, 1, 3]) # order not guaranteed


unique_data = []

for ele in data:
   if ele not in unique_data:
      unique_data.append(ele)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed

#is there a better way with using a set?
# sort key?

