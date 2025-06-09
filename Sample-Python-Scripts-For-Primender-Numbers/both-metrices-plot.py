import sympy as sp
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(n):
    return sp.isprime(n)

# Function to generate the Primender sequence
def generate_primender_sequence(limit):
    primender_sequence = []
    for n in range(1, limit + 1):
        if is_prime(n) or n % 10 in {2, 3, 5, 7} or is_prime(n % 100) or is_prime(n % 1000):
            primender_sequence.append(n)
    return primender_sequence

# Function to compute the largest prime less than or equal to a given number
def largest_prime_leq(n):
    return sp.prevprime(n + 1)

# Generate the first 1000 Primender numbers
primender_sequence = generate_primender_sequence(1000)

# Compute Delta (PEn - PEn-1)
deltas = [primender_sequence[i] - primender_sequence[i - 1] for i in range(1, len(primender_sequence))]

# Compute PEn - LPn
pen_lpn_values = [primender_sequence[i] - largest_prime_leq(primender_sequence[i]) for i in range(len(primender_sequence))]

# Plot the values
plt.figure(figsize=(12, 6))
plt.plot(range(1, len(primender_sequence)), deltas, label='Delta (PEn - PEn-1)', color='blue')
plt.plot(range(len(primender_sequence)), pen_lpn_values, label='PEn - LPn', color='orange')
plt.xlabel('Index n')
plt.ylabel('Values')
plt.title('Delta and PEn - LPn Values for the First 1000 Primender Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
