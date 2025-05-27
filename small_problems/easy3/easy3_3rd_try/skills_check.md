- Question 1:

```python

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)

```
- This is mostly math; need to % remainder to round to 1 day or add 1440 to reduce negative days
- afterwards // to get hours floor division
- or % remainder to get mins

- Question 2:

```python

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0

    return delta_minutes

```

- Had help with original algorithm for math
- reverse engineered


- ***Question 3:

```python

def repeater(string):
    return ''.join([char * 2 for char in string])

```

- use list comprehension and then join method to attach string

- Question 4:

```python

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(string):
    result = []

    for char in string:
        if char.lower() in CONSONANTS:
            result.append(char * 2)
        else:
            result.append(char)

    return ''.join(result)

```

- same as I did but with consonant instead of isalpha and VOWELS


- Question 5:

```python

def reverse_number(number):
    return int(str(number)[::-1])

```

- Answered the same as I did, convert to string to reverse turn back to integer

 - ***Question 6:

 ```python

 def sequence(limit):
    return list(range(1, limit + 1))

```

- Use a list constructor to create the range list- I used a comprehension

- ***Question 7:

```python

def swap_name(name):
    return ', '.join(name.split()[::-1])

```

- They used a reversal and rejoin using ', ' 

- Question 8:

```python

def sequence(count, start_num):
    return [start_num * num for num in range(1, count + 1)]
```

- uses a multiple for the start numb and mutiplies by the range. + 1 to be inclusive


- Question 9:

```python
def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    return lst

def reverse_list(lst):
    n = len(lst)
    for idx in range(n // 2):
        lst[idx], lst[-(idx + 1)] = lst[-(idx + 1)], lst[idx]

    return lst

```

- Uses a while and adjust the indices during the loop
- uses a negative index instead of index to go reverse same as my approach

- ***Question 10:

```python

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0

```

- Uses the condition if the "count" parens is ever negative to return False. 