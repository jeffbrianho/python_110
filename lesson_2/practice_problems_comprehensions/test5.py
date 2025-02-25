employees = {
    'Engineering': {'Alice': {'salary': 80000, 'years_experience': 5},
                    'Bob': {'salary': 75000, 'years_experience': 3}},
    'Marketing': {'Charlie': {'salary': 70000, 'years_experience': 4},
                  'David': {'salary': 65000, 'years_experience': 2}}
}

# Use a comprehension to create a list of all employees who have more than 3 years of experience.

"""
list of employees that have > 3 years

[alice, charlie]

"""

# lst = []
# for dept, subdict in employees.items():
#     for name, inner_subdict in subdict.items():
#        if inner_subdict['years_experience'] > 3:
#            lst.append(name)

            
lst = [name for subdict in employees.values()
       for name, inner_subdict in subdict.items()
       if inner_subdict['years_experience'] > 3]

print(lst)