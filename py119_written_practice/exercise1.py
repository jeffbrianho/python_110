# Basic​: Explain the difference between sorted() function and the list.sort() 
# method in Python. Include an example of when you would use each.

"""
# The difference between `sorted()` function and `list.sort()` method is how it will interact with the data structure.
# The function will return a sorted data structure without mutating the orignal structure. It will also return the sorted structure
# upon the function call.  The method will
# mutate a list in place and return None. 

"""

#  ​Intermediate​: Consider the following nested data structure:
   
people = [
  {'name': 'Alice', 'scores': [85, 90, 77]},
  {'name': 'Bob', 'scores': [92, 88, 95]},
  {'name': 'Charlie', 'scores': [75, 80, 82]}
]
    
#    Write a comprehension that creates a new list containing the names of 
# people who have at least one score above 90.

# new_people_list = [person['name'] for person in people
#                    if any([score for score in person['scores'] if score > 90])]
# print(new_people_list)

# new_people_list = [person['name'] for person in people
#                   if any(score > 90 for score in person['scores'])] # make boolean immediately


#   ​Intermediate​: Explain the difference between shallow copy and deep copy in Python. 
# Provide an example scenario where using the wrong type of copy could lead to unexpected behavior.

# The difference between a shallow copy and a deep copy is how it affects nested collections
# a shallow copy will only create a true copy of an outer collection where as any nested collection will 
# reference the object and share the same heap address. any changes made to the nested object will be reflected in both 
# original and copy.  A deep copy will, however make a true copy of the whole collection and nested collections. If
# changes are made to either a copy or an original, it will not be reflected in the other. 

# if trying to make changes to a nested list `lst = [[1,2], [3, 4]]` and a copy is made
# `copy_lst = lst[:]`
# when mutating the copy_lst with something like copy_lst[0].append(3).
# both will have the 3 appended to the first list.
#`print(copy_lst, lst) # [[1, 2, 3], [3, 4]]`
# the benefits of a shallow copy is that it saves memory but if you need to modify an inner structure while maintaining the
# orginal, a deep copy would be preferable

# lst = [[1,2], [3, 4]]
# copy_lst = lst[:]
# copy_lst[0].append(3)
# print(copy_lst, lst)


#   ​Advanced​: Given the following code:
   
students = [
  {'name': 'Emma', 'grade': 'A', 'courses': ['Math', 'Science']},
  {'name': 'James', 'grade': 'B', 'courses': ['History', 'English', 'Art']},
  {'name': 'Olivia', 'grade': 'A', 'courses': ['Math', 'English']},
  {'name': 'Noah', 'grade': 'C', 'courses': ['Science', 'History']}
]
    
#    Write code using sorting functions to:
#    1.  Sort the students by the number of courses they're taking (in descending order)
#    2.  If two students are taking the same number of courses, sort them alphabetically by name

def return_course_amount(dictionary):
    return len(dictionary['courses'])

def return_name(dictionary):
    return dictionary['name']

print(sorted((sorted(students, key=return_name)), key=return_course_amount, reverse=True))