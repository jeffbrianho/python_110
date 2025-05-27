# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater 
# than the length of the longest side, and every side must have a length greater than 0. 
# If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments 
# and returns one of the following four strings representing the triangle's classification: 
# 'equilateral', 'isosceles', 'scalene', or 'invalid'.


"""
P:
I: 3 lengths of sides as arguments
O: string as 'equilateral', 'isosceles', 'scalene', or 'invalid'.

E
I

E: use definitions
D: list?

A:
add each argument to a list:
check for neither:
if 0 - invalid
if iterate 1 == same .count? =2 or 3 print accordingly

for max(num) pop it and compare to sum of rest if sum > pop scalene
else invalid
C

"""

def triangle(s1, s2, s3):
    lst = [s1, s2, s3]

    
    if 0 in lst or (sum(lst) - max(lst)) < max(lst):
        return 'invalid'
    elif lst.count(s1) == 2 or lst.count(s2) == 2:
        return 'isosceles'
    elif lst.count(s1) == 3:
        return 'equilateral'
    elif (sum(lst) - max(lst)) > max(lst):
        return 'scalene'
    else:
        return 'invalid'
    


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# their answer

def get_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "scalene"

def is_valid(shortest, middle, longest):
    return shortest > 0 and shortest + middle > longest

def triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    longest = max(side1, side2, side3)
    shortest = min(side1, side2, side3)
    middle = perimeter - longest - shortest

    if is_valid(shortest, middle, longest):
        return get_triangle_type(side1, side2, side3)
    else:
        return "invalid"
    
    # Their answer

def get_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "scalene"

def is_valid(shortest, middle, longest):
    return shortest > 0 and shortest + middle > longest

def triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    longest = max(side1, side2, side3)
    shortest = min(side1, side2, side3)
    middle = perimeter - longest - shortest

    if is_valid(shortest, middle, longest):
        return get_triangle_type(side1, side2, side3)
    else:
        return "invalid"
    
# second attempt t18:23 took time for logic 

def triangle(side1, side2, side3):
    triangle_list = [side1, side2, side3]

    def is_triangle(lst):
        return max(lst) < (sum(lst) - max(lst))

    if is_triangle(triangle_list):
        if  all([x == triangle_list[0] for x in triangle_list]):
            return 'equilateral'
        if any(triangle_list.count(x) == 2 for x in triangle_list):
            return 'isosceles'
        if all([triangle_list.count(x) == 1 for x in triangle_list]):
            return 'scalene'

    else:
        return 'invalid'
    