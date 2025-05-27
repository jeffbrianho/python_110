- Question 1:

```python

NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_for_number(num):
    return NUMBER_WORDS[num]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_for_number)

```

- Same answer, use a key to return the string

- Question 2:

```python

def merge_sets(list1, list2):
    return set(list1) | set(list2)

```

- same answer convert with set constructor and use method union

- Question 3:

```python

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

```

- frozenset conversion and & for intersection

- Question 4:

```python

def sort_key(item):
    return item[1]

def order_by_value(d):
    sorted_items = sorted(d.items(), key=sort_key)
    return [key for key, value in sorted_items]

```

- they turn a tuple and sort by second index, then create a list in the sorted item. 

```python


def order_by_value(dictionary):

    def key_sort(key):
        return dictionary[key]
    
    return sorted([key for key in dictionary], key=key_sort)


```
- I like mine better

- Question 5:

```python

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

```

- same answer, set conversion and difference of caller to argument

- Question 6:

```python

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

```

- use index to get sub string with same starting point and incrementing end point

- Question 7:

```python

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]
```

- uses leading substrings to get each substring for a starting letter
- second function starts at 0 an increments up

- Question 8:

```python
def create_substrings(string):
    return [string[start:end] for start in range(len(string))
                            for end in range(start + 1, len(string) + 1)]

def palindromes(string):
    return [substring for substring in create_substrings(string)
                    if substring == substring[::-1] and len(substring) > 1]

```
- This is mine, create substrings and then select based on palindrome and length

```python

def is_palindrome(word):
    return len(word) > 1 and word == word[::-1]

def palindromes(s):
    return [substring
            for substring in substrings(s)
            if is_palindrome(substring)]

```

- They create a function that defines length and palindrome I put it directly into selection criteria


- Question 9:

```python

def transactions_for(inventory_item, transactions):
    return [transaction
            for transaction in transactions
            if transaction["id"] == inventory_item]

```

- same as min

- Question 10:

```python

def is_item_available(item, transactions):
    relevant_transactions = transactions_for(item, transactions)
    quantity = 0

    for transaction in relevant_transactions:
        if transaction["movement"] == 'in':
            quantity += transaction["quantity"]
        else:
            quantity -= transaction["quantity"]

    return quantity > 0

```

- same thing but I made a separate function for quantity. 