def fibonacci(num):
    previous_num = 1
    current_num = 1

    if num <= 2:
        return 1

    for _ in range(3, num + 1):
        previous_num, current_num = current_num, previous_num + current_num

    return current_num

# is fibonacci create a list or tuple to hold value and if index in in the value return

def is_fibonacci(num):
    return num in (fibonacci(num) for num in range(num + 5))

def list_fib(lst):
    return [lst[indx] for indx in range(len(lst))
            if is_fibonacci(indx)]

print(list_fib([1, 2, 3, 4, 5, 6])) 