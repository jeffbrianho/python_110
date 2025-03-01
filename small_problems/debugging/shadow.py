# We defined a function intending to multiply the sum of numbers by a factor. 
# However, the function raises an error. Why? How would you fix this code?

def fac_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(fac_sum(numbers, 2) == 20)

# dont use the same name for a function that already exists and try to use it in the code