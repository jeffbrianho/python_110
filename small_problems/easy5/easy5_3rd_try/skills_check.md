- Question 1:

```python

def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

```
- invert using items method for tuple dict view

- ***Question 2:

```python

def keep_keys(my_dict, key_list):
    return {key: my_dict[key]
            for key in key_list
            if key in my_dict}

```
- don't forget about dict[key] access

- ***Question 3:

```python

def strip_vowels(string):
    VOWELS = "aeiouAEIOU"
    no_vowels = [char for char in string
                 if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(string_list):
    return [strip_vowels(string) for string in string_list]

```
- Dont forget you can use ''.join to make a string from a list of chars

- Question 4:

```python

def word_lengths(string=''):
    if not string:
        return []

    return [f"{word} {len(word)}"
            for word in string.split()]
```

- same

- Question 5:

```python

def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

def multiply_items(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])

    return result

```
- can use zip and a tuple unpacking
- i used a range 

- ***Question 6:

```python
def sum_of_sums(numbers):
    total_sum = 0
    running_sum = 0
    for num in numbers:
        running_sum += num
        total_sum += running_sum

    return total_sum
```

- They use a nested sum; keep storage of added sum and add to an ultimate final count

- Question 7:

```python

def sum_digits(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digits)
```

- str_num will return a stirng you can iterate through ;

- Question 8 :

```python
def staggered_case(string):
    result = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower
        result += func()

    return result

```
- idk why they chose to make the func() opposed to upper() and lower()

- Question 9:

```python

def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

    return result

```

- same as me but put coditional in result+= 

- ***Question 10:

```python

def unique_sequence(numbers):
    return [value
            for idx, value in enumerate(numbers)
            if idx == 0 or value != numbers[idx-1]]

```

- References same list with value and indx-1