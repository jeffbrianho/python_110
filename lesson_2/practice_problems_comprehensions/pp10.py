# Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string.
#  The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 
# 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

# Write a function that takes no arguments and returns a string that contains a UUID.

from random import randint


CHAR_LIST = list('abcdefghijklmnopqrstuvwxyz0123456789')

def UUID():
    final_string = ''
    for _ in range(8):        
        rand_digit = (randint(0, len(CHAR_LIST) - 1))
        final_string += CHAR_LIST[rand_digit]
    final_string += '-'
    
    count = 0
    while count < 3:
        for _ in range(4):        
            rand_digit = (randint(0, len(CHAR_LIST) - 1))
            final_string += CHAR_LIST[rand_digit]
        final_string += '-'
        count += 1

    for _ in range(12):        
        rand_digit = (randint(0, len(CHAR_LIST) - 1))
        final_string += CHAR_LIST[rand_digit]
   
    return final_string

print(len(''.join(UUID().split("-"))))

#Their code

import random

def generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

# Outputs shown below are samples - you output will vary
print(generate_uuid())  # '02e51c2f-dacd-c319-53b5-e40e6e8c1f78'
print(generate_uuid())  # '39038ab9-3b95-43d8-6959-5d785ccb9b69'
print(generate_uuid())  # 'f7d56480-c5b2-8d4d-465f-01a4ea605729'