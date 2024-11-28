# Write a Python function that finds all prime numbers up to a given number n.
#
# Function Requirements:
#
# The function should take a single integer n as input.
#
# It should return a list of all prime numbers less than or equal to n.

from art import logo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Example usage
print(logo)
n = int(input("Enter a number to find all prime numbers up to: "))
prime_numbers = find_primes_up_to(n)
print(f"Prime numbers up to {n}: {prime_numbers}")
