# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to check if a number is a Primender
def is_primender(n):
    return is_prime(n) or n % 10 in {2, 3, 5, 7} or is_prime(n % 100) or is_prime(n % 1000) or is_prime(n % 10000) or is_prime(n % 100000)

# Generate the first 100000 Primender numbers
primender_numbers = []
n = 1
while len(primender_numbers) < 100000:
    if is_primender(n):
        primender_numbers.append(n)
    n += 1

# Compute delta values
deltas = [primender_numbers[i] - primender_numbers[i - 1] for i in range(1, len(primender_numbers))]

# Function to find the largest prime less than or equal to a given number
def largest_prime_less_than_or_equal_to(n):
    for i in range(n, 1, -1):
        if is_prime(i):
            return i
    return None

# Verify the hypothesis
hypothesis_holds = True
for i in range(1, len(primender_numbers)):
    PEn = primender_numbers[i]
    LPn = largest_prime_less_than_or_equal_to(PEn)
    if PEn - LPn == 1:
        if deltas[i - 1] != 1:
            hypothesis_holds = False
            print(f"Hypothesis fails at PEn = {PEn}, LPn = {LPn}, Delta = {deltas[i - 1]}")
            break

if hypothesis_holds:
    print("The hypothesis holds for the first 100000 Primender numbers.")
else:
    print("The hypothesis does not hold for the first 100000 Primender numbers.")
