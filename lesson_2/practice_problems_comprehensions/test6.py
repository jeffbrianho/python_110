# Using the same employees dictionary, create a dictionary comprehension that calculates 
# the average salary for each department.

employees = {
    'Engineering': {'Alice': {'salary': 80000, 'years_experience': 5},
                    'Bob': {'salary': 75000, 'years_experience': 3}},
    'Marketing': {'Charlie': {'salary': 70000, 'years_experience': 4},
                  'David': {'salary': 65000, 'years_experience': 2}}
}


""" 

o: {dept: avg sal}
{Engineering: 77750, Marketing: 67750}
"""
# final_dict = {}
# for dept, subdict in employees.items():
#     avg_salary = 0
#     for exp in subdict.values():
#         avg_salary += exp['salary']
#     final_dict[dept] = (int(avg_salary/len(subdict)))


# for dept, emps in employees.items():
#     print(int(sum([emp['salary'] for emp in emps.values()])/ len(emps)))
    

final_dict = {dept: int(sum([emp['salary'] for emp in emps.values()])/ len(emps)) for dept, emps in employees.items()
              }
print(final_dict)