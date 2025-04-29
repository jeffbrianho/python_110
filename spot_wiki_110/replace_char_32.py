# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

"""
P:
I: string
O: return a string of numbers
E
I

E
D
A:

make your reference list
make a list of chars:
for each char replace with num from reference list.
join list


"""


def alphabet_position(sentence):
    REFERENCE = list(' abcdefghijklmnopqrstuvwxyz')

    char_list = list(sentence)
    num_list = []

    for char in char_list:
        if char.isalpha():
            if REFERENCE.index(char.lower()):
                num_list.append(str(REFERENCE.index(char.lower())))

    return ' '.join(num_list)

print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("-.-'") == "")