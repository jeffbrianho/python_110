- Question 1:

```python
DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string

def dms(degrees_float):
    degrees_int = int(degrees_float)
    minutes = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
    seconds = int(
        (degrees_float - degrees_int - (minutes / MINUTES_PER_DEGREE)) *
        SECONDS_PER_DEGREE
    )

    return (f"{degrees_int}{DEGREE}"
            f"{pad_zeroes(minutes)}'"
            f'{pad_zeroes(seconds)}"')
```

- manually create the padded zeros with a custom function
    - if the number is less than 2 concatenate a zero at beginning of number
- I used the divmod to address the remainder but they used `int` to get whole number and subtract the float to work with decimal. `seconds` is a bit more tricky, subtract the whole number  to get remainder idk how they got the seconds. I like my way better

- Question 2:

```python
def copy_non_dups_to(result_set, lst):
    for value in lst:
        result_set.add(value)

def union(list1, list2):
    result_set = set()
    copy_non_dups_to(result_set, list1)
    copy_non_dups_to(result_set, list2)
    return result_set

def union(list1, list2):
    return set(list1).union(set(list2))

```

- The first method seems too long. They created an append(add) method to a set.
- Second is more like mine but use the actual `union` method where I use `|`

- Question 3:

```python
def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]
```

- To avoid an if statement they increment the num by 1 then divide by 2 therefore adding the element to the first half of the list, as // rounds down. 

- Question 4:

```python
def find_dup(lst):
    seen = set()

    for element in lst:
        if element in seen:
            return element

        seen.add(element)

def find_dup(lst):
    dups = [element for element in lst if lst.count(element) == 2]
    return dups[0]
```

- The first method uses a storage and if it is seen return the number. if not seen add number to storage
    - probably the easiest way to iterate through a list

- The second way is similar to how I did but uses a list comprehension and returns the element of the list using indexing of `[0]`

- ***Question 5:

```python
def interleave(list1, list2):
    new_list = []
    for idx in range(len(list1)):
        new_list.extend([list1[idx], list2[idx]])

    return new_list
```

- Use extend method and add 2 at the same time as opposed to appending separately

- Question 6:

```python 

def round_to_three_digits(number):
    rounded_number_as_str = str(round(number, 3))
    decimal_position = rounded_number_as_str.find('.')

    while len(rounded_number_as_str) - decimal_position < 4:
        rounded_number_as_str += '0'

    return rounded_number_as_str

def multiplicative_average(numbers):
    product = 1

    for num in numbers:
        product *= num

    return round_to_three_digits(product / len(numbers))

def round_to_three_digits(number):
    return f"{number:.3f}"

# multiplicative_average doesn't change

```
- they round using `round` string function. round, digits. finds the decimals

- Question 7:

```python

def multiply_list(numbers1, numbers2):
    result = []

    for i in range(len(numbers1)):
        result.append(numbers1[i] * numbers2[i])

    return result

def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]
```

- They answer the same as I do but then use zip and tuple unpacking to get multiple as they iterate each tup

- Question 8:

```python

def digit_list(number):
    return [int(digit) for digit in str(number)]

```
- I answered the same way, just need to be careful with variable names


- ***Question 9:

```python

def print_occurrences(occurrences):
    for item, count in occurrences.items():
        print(f"{item} => {count}")

def count_occurrences(elements):
    occurrences = {}

    for item in elements:
        occurrences[item] = occurrences.get(item, 0) + 1

    print_occurrences(occurrences)

```

- They use a dictionary creation to make their count
    - if items exists reassign it plus 1 if it doesn't create 0 + 1

- Question 10:

```python

def average(numbers):
    total = sum(numbers)
    return total // len(numbers)

```
- Pretty straight forward maths


