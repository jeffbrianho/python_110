- ***Question 1:

```python
numbers = []

numbers.append(input("Enter the 1st number: "))
numbers.append(input("Enter the 2nd number: "))
numbers.append(input("Enter the 3rd number: "))
numbers.append(input("Enter the 4th number: "))
numbers.append(input("Enter the 5th number: "))
last_number = input("Enter the last number: ")

numbers_list = ','.join(numbers)

if last_number in numbers:
    print(f"{last_number} is in {numbers_list}.")
else:
    print(f"{last_number} isn't in {numbers_list}.")
```
- Using append with the input as a function composition
- Do not forget to use the `','` join method to create a string

- Question 2:

```python
def is_palindrome(s):
    return s == s[::-1]
```
 - Use of the reverse step slicing method (it is a shallow copy)

 - Question 3:

 ```python
 def is_real_palindrome(s):
    cleaned_string = ''
    for char in s:
        if char.isalnum():
            cleaned_string += char.casefold()

    return is_palindrome(cleaned_string)
```

- Use of an iteration to create a cleaned string
- Can use `casefold()` for the concatenation and not worry about changing the iterable

- Question 4:

```python
def running_total(nums):
    result_list = []
    total = 0

    for num in nums:
        total += num
        result_list.append(total)

    return result_list

    #### second answer

    return [sum(nums[:indx]) for range(1,len(nums) + 1)]
```

- Use a reassignment to add the last num to the next for a running total
- Can use a range and a slice to grow the slice i.e `# nums[:indx] = [1], nums[:indx + 1] = [1, 2],` 
                                                    `nums[:indx + 2] == [1, 2, 3]`


- ***Question 5:

```python

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

        # counts[word_size] = counts.get(word_size, 0) + 1

    return counts
```

- Uses dictionary key assignment for numbers then adds by a counter 

- Question 6:

```python
def remove_non_letters(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char

    return result

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        clean_word = remove_non_letters(word)

        clean_word_size = len(clean_word)
        if clean_word_size == 0:
            continue

        if clean_word_size not in counts:
            counts[clean_word_size] = 0

        counts[clean_word_size] += 1

    return counts
```

- Cleans the string from nonalpha chars
- Uses function to clean word to create the dictionary, same way to create using dictionary key reassignment

- ***Question 7:

```python
def swap(words):
    words_list = words.split()

    for idx in range(len(words_list)):
        words_list[idx] = swap_first_last_characters(words_list[idx])

    return ' '.join(words_list)

def swap_first_last_characters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]
```

- Uses a helper function to create the new string
    - You can get the middle number with `[1:-1]` 
- Reassign a new string in place with list index reassignment 

- ***Question 8:

```python
def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]

    return value
```

- Use a map to get the digit value
- Uses reassignment with the value times 10 and adding the end digit to build the number

- Question 9:

```python
def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)
```

- Isolate the single first index of the string and use a match, case
    - Then use slicing to get the appropriate portion of the string
    - `_` case for everything else

- ***Question 10:

```python
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'
```
- Uses list and indexing to obtain string value at corresponding index
- Use the divmod function to get a tuple including the num divided by the second argument and the remainder
    - `# divmod(1234, 10) => (123, 4): this will get the input from right to left
- Use tuple reassignment to reassign the number and work with the remainder
- append the digits left to right using (result = NEW_NUM + result ) - need to append backwards due to the divmod
    - slicing from right to left

- Question 11:

```python
def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"
```

- Use f-strings to add the corresponding needed string with if statements
- use `-` directly into {} to reverse the negative number

