# Write a function that takes a string argument consisting of a first name, a space, 
# and a last name. The function should return a new string consisting of the last name, a 
# comma, a space, and the first name.

"""
P
I string first name space lastname
O string lastnaem comma space firstname 
E only strings?
I

E
D
A: strings use split into list input f string



"""
def swap_name(name):
    list_name = name.split()
    return (f'{list_name[-1]}, {' '.join(list_name[0:-1])}')

#their answer
# def swap_name(name):
#     return ', '.join(name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals'))#
                # == "Ragvals, Karl Oskar Henriksson")  # True