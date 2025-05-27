- Question 1:

```py
def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if len(lst) == 0:
        return []

    return lst[1:] + [lst[0]]

```

- they used same answer but more distinct if statements. 
- theirs is cleaner and easier to read

- ***Question 2:

```py
def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]
```

- They split the string into a substring starting at the count and then rotate to the end and concatenate
- I removed the element combined the leftover and added to the end. mine is more complicated when rotations happen at 1
    - able to solve with conditional

- Question 3:

```py
def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number
```

- I had that as an answer but my helper function did not work like theirs did. spent time recoding the helper function to maintain the arguement as a string

- Question 5:

```py

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUM_WORDS.get(word, word) for word in words]
    return ' '.join(processed_words)

```

- did the same way; 
- use of dict method get.(word,  word)

- Question 7:

```py

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current

```