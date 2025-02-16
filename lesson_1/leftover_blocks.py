# Step 1: Understand the Problem

# Leftover Blocks:
# You have a number of building blocks that can be used
# to build a valid structure.
# There are certain rules about what determines a 
# valid structure:
#   - The building blocks are cubes
#   - The structure is built in layers
#   - The top layer is a single block
#   - A block in an upper layer must be support by four blocks in a lower layer
#   - A block in a lower layer can support more than one block in an upper layer
#   - You cannot leave gaps between blocks. ]
#
# Write a program that, given the number of availalbe blocks, calculates the number of blocks left over
# after building the tallest possible valid structure
#
# TASKS: You are provided with the problem description above.
# Your tasks for this step are:
# 
#   - Make notes of your mental model for the problem, including, 
#       - input and outputs
#       - explicit and implicit rules
#   - Write a list of clarifying questions for anything that isn't clear

'''

P: 
Input: an integer of number of blocks
Output: return an integer of remainder of blocks following tallest strucuture
Explicit: Top layer is 1 block follwed by 4 blocks underneath
          x
       x x x x
    x x x x x x x 
 x x x x x x x x x x
  blocks can support more than 1 block no gaps between blocks
Implicit: only enough support to make a uniform triangle ie. cannot just have
a single ext with a box underneath of 4

will be provided a single integer

Questions: will it be a triangle? must the 4 supporting 1 be adjacent?


THEIR ANSWER:
- Input: integer for a specific amount of blocks
- Output: integer for left over blocks after building the tallest
  possible valid structure

- Structures are built with blocks:
    - Blocks are cubes.
    - Cubes are six-sided, have square faces, and have equal
      lengths on all sides.
- The top layer in the structure consists of a single block.
- Upper layer blocks must be supported by four lower layer blocks.
- Lower layer blocks can support more than one upper layer block.
- Layers are solid structures -- there are no gaps between blocks.

*** its a three dimentional structure

Layer 1: 1 block (1x1)
Layer 2: 4 blocks (2x2)
Layer 3: 9 blocks (3x3)

Implicit rules:
- Layer number correlates with blocks in a layer:
- The number of blocks in a layer is layer number * layer number.

Questions: 
Can we add more than 4 blocks?
Will there always be blocks left over?

- Is a lower layer valid if it has more blocks than it needs?
- Will there always be left-over blocks?



'''

# Step 2: Examples and test cases
# You are provided test cases for the problem:

# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

'''
E:
blocks appear to follow the squares of each number summed and the remainder is left for our
return value. There will only be enough to meet the 4 sides no more, no less
There will not always be leftover blocks; can leave 0

'''

# Step 3: Data Structures
# Use analysis so far whether you need to use data structures

'''
D:
potential nested lists for number of cubes used per layers

"""
- Perhaps we can use a nested list to represent the structure?
    - Each sublist could represent a layer.
"""

[
    ['x'],
    ['x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
      ...
]
'''

# Step 4: Algorithm
# Write a high-level algoithm that solves the problem
# at an abstract level. 

'''
A:
With a give integer input
helper function? create an array that contains numbers of progressive cubes
subtract the nearest amount of the numbers the the given integer
return the remainder
if number = input, return 0

1. Build the structure one layer at a time until you no longer
   have enough blocks left to build a "valid" layer.
2. Count how many blocks you have left.


PROGRAMMATIC ALGORTHIM
1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 1.
     - The "number of blocks required in this layer" is 1.

2. Subtract the "number of blocks required in this layer" from
   the "number of blocks remaining".

3. Calculate the "current layer number" for the next layer by
   adding 1 to the "current layer number".

4. Using the new "current layer number", calculate the "number of
   blocks required in this layer" by multiplying the "current
   layer number" by itself.

5. Determine whether the "number of blocks remaining" is greater
   than or equal to the "number of blocks required in this layer".
     - If there are enough blocks:
         - Subtract the "number of blocks required in this layer"
           from the "number of blocks remaining".
         - Go to step 3.
     - If there aren't enough blocks:
         - Return the "number of blocks remaining".

Will be left with -1 if using a 0 layer: MUST CORRECT ***

1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 0.

2. Calculate the "current layer number" for the next layer by
   adding 1 to the "current layer number".

3. Using the new "current layer number", calculate the "number of
   blocks required in this layer" by multiplying the "current
   layer number" by itself.

4. Determine whether the "number of blocks remaining" is greater
   than or equal to the "number of blocks required in this layer".
     - If there are enough blocks:
         - Subtract the "number of blocks required in this layer"
           from the "number of blocks remaining".
         - Go to step 2.
     - If there aren't enough blocks:
         - Return the "number of blocks remaining".

'''

def calculate_leftover_blocks(blocks):
    number_of_blocks_remaining = blocks
    current_layer = 0

    number_of_blocks_for_layer = current_layer**2
    
    while number_of_blocks_remaining >= number_of_blocks_for_layer:
        number_of_blocks_remaining -= number_of_blocks_for_layer
        current_layer += 1
        number_of_blocks_for_layer = current_layer**2
    
    return number_of_blocks_remaining


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
