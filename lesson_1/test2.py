

def multiply(numbers, multiple):
    doubled_nums = []

    for num in numbers:
        doubled_nums.append(num * multiple)

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]