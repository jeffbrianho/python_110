# Write a function that counts the number of occurrences of each element in a 
# given list. Once counted, print each element alongside the number of occurrences. 
# Consider the words case sensitive e.g. ("suv" != "SUV").

"""
P:
I: list with elements
O: ?string with number of occurences
E: case matters
I:
Q:

E
D: dictionary?
A:
create a dictionary with key as word and count as value
upack and print key value in string

C


"""


def count_occurrences(old_lst):
    my_dict = {}

    lst = [] 
    for ele in old_lst:
        lst.append(ele.casefold())

    for element in lst:
        my_dict[element] = lst.count(element)

    for key, value in my_dict.items():
        print(f'{key} => {value}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

count_occurrences(vehicles)


# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2