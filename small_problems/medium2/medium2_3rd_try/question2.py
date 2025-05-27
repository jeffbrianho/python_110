# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
# To be a valid triangle, the sum of the lengths of the two shortest sides must 
# be greater than the length of the longest side, and every side must have a length 
# greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments 
# and returns one of the following four strings representing the triangle's classification: 
# 'equilateral', 'isosceles', 'scalene', or 'invalid'.

"""
a:
def is_valid(num num num):
for max num < sum total mins max
if num for num in list is 0 - fALSE

if all[lst[0] == comparative for comparative in lst[1:]]
    equal
if [].count(True) == 2
iso
if not all[]
scalene

"""

def triangle(side1, side2, side3):
    side_list = [side1, side2, side3]

    def is_triangle(side_list):
        
        for side in side_list:
            if side == 0 or max(side_list) > (sum(side_list) - max(side_list)):
                return False
        
        return True

    if is_triangle(side_list):
        if all([side_list[0] == side for side in side_list]):
            return 'equilateral'
        elif [side_list[0] == side for side in side_list].count(True) == 2:
            return 'isosceles'
        elif [side_list[0] == side for side in side_list].count(True) == 1:
            return 'scalene'
    else:
        return 'invalid'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True