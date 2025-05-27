# Create a generator expression to yield all prime numbers less than 50.

def is_prime(num):
    if num <= 1:
        return False
    
    return all([num % div != 0 for div in range(2, int(num**0.5) + 1)])

print((num for num in range(1, 50) if is_prime(num)))