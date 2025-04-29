# A triangle is classified as follows:

# Right: One angle is a right angle (exactly 90 degrees).
# Acute: All three angles are less than 90 degrees.
# Obtuse: One angle is greater than 90 degrees.
# To be a valid triangle, the sum of the angles must be exactly 180 degrees, 
# and every angle must be greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the three angles of a triangle as arguments and returns one of the 
# following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

# You may assume that all angles have integer values, so you do not have to worry about floating point errors. 
# You may also assume that the arguments are in degrees.


"""
I: 3 angles integers
O: string right, acute, obtuse, invalid

A: is valid?
sum of all numbers == 180
no number is 0 in list
check type:
if 90 in list return right iterate
if any is greater than 90 return obtuse
else return acute

"""

def valid_angle(deg1, deg2, deg3):
    if (deg1 + deg2 + deg3) == 180 and 0 not in (deg1, deg2, deg3):
        return True
    return False

def triangle(ang1, ang2, ang3):
    if valid_angle(ang1, ang2, ang3):
        if ang1 == 90 or ang2 == 90 or ang3 == 90:
            return "right"
        elif ang1 > 90 or ang2 > 90 or ang3 > 90:
            return "obtuse"
        else:
            return "acute"
    return "invalid"

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Their answer

def is_right_triangle(angle):
    return angle == 90

def is_acute_triangle(angle):
    return angle < 90

def get_triangle_type(angles):
    if any([is_right_triangle(angle) for angle in angles]):
        return "right"
    elif all([is_acute_triangle(angle) for angle in angles]):
        return "acute"
    else:
        return "obtuse"

def is_valid(angles):
    total_angle = sum(angles)
    all_non_zero = all([angle > 0 for angle in angles])
    return total_angle == 180 and all_non_zero

def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    if is_valid(angles):
        return get_triangle_type(angles)
    else:
        return "invalid"
    
    # treat as list and booleans
    