def binary_search(lst, item):
    new_lst = lst[:]
    index = 0

    while len(new_lst) > 1:
        if new_lst[0] == item:
            return 0
        elif new_lst[(len(new_lst) // 2)] == item:
            index += len(new_lst) // 2
            return index
        elif new_lst[(len(new_lst) // 2)] < item:
            index += (len(new_lst) // 2)
            del new_lst[:(len(new_lst) // 2)] 
        else:
            del new_lst[(len(new_lst) // 2):] # [1, 2, 3]
            
    return -1



print(binary_search([1, 2, 3, 4, 5, 6], 1))

# # All of these examples should print True
# businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
#               'Donuts R Us', 'Eat a Lot', 'Good Food',
#               'Pasta Place', 'Pizzeria', 'Tiki Lounge',
#               'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
#          'Tyler']
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)

# Their answer:
def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == search_item:
            return mid
        elif lst[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1