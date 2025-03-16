
# Implement a function that adds two numbers together and returns their
#  sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

def add_binary(a,b):
    bin_sum = a + b
    current_sum = bin_sum
    final_bin = '0' 

    while current_sum > 0:
        if final_bin[0] == '1':
            final_bin = '0' + final_bin
            final_bin[0] = '0'
            final_bin 
            
        final_bin += 1

print(add_binary(1, 1))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary