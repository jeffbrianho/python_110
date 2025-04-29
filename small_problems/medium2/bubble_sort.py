# Bubble Sort is one of the simplest sorting algorithms available.
#  It is not an efficient algorithm, so developers rarely use it in real code.
#  However, it is an excellent exercise for student developers. In this exercise, 
# you will write a function that sorts a list using the bubble sort algorithm.

# A bubble sort works by making multiple passes (iterations) through a list. On each pass, 
# the two values of each pair of consecutive elements are compared. If the first value is greater 
# than the second, the two elements are swapped. This process is repeated until a complete pass is made
#  without performing any swaps. At that point, the list is completely sorted.

#We can stop iterating the first time we make a pass through the list without making any swaps since 
# that means the entire list is sorted.

# For further information -- including pseudo-code that demonstrates the algorithm, 
# as well as a minor optimization technique -- see the Bubble Sort Wikipedia page.

# Write a function that takes a list as an argument and sorts that list using the 
# bubble sort algorithm described above. The sorting should be done "in-place" -- 
# that is, the function should mutate the list. You may assume that the list contains at least two elements.

"""
I: elements in a list
O: mutated sorted list
keep swapping until elements are < in order


mutating methods list insert?>

while counter == True:
counter = False
iterate through list if [a]indx1 is > [b]indx2
    perform swap [b]indx 1 and [a]indx2
    counter = True
    return lst
"""
def bubble_sort(lst):
    counter = True
    while counter == True:
        counter = False
        for indx, element in enumerate(lst):
            if indx != (len(lst) - 1) and element > lst[indx + 1]:
                lst[indx], lst[indx + 1] = lst[indx + 1], element
                counter = True

lst1 = [5, 3]
bubble_sort(lst1)
print((lst1) == [3, 5])                # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

# Their answer
def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(1, len(lst)):
            if lst[idx - 1] <= lst[idx]:
                continue

            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            swapped = True

        if not swapped:
            break