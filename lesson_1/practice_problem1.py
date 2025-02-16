fruits = ("apple", "banana", "cherry", "date", "banana")

#print(fruits.count('banana'))

count = 0
for fruit in fruits:
    if fruit == 'banana':
        count += 1

print(count)