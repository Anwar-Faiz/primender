import matplotlib.pyplot as plt

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
    return is_prime(n) or n % 10 in {2, 3, 5, 7} or is_prime(n % 100) or is_prime(n % 1000)

# Generate the first 10,000 Primender numbers
primender_numbers = []
n = 1
while len(primender_numbers) < 100000:
    if is_primender(n):
        primender_numbers.append(n)
    n += 1

# Compute delta values
deltas = [primender_numbers[i] - primender_numbers[i - 1] for i in range(1, len(primender_numbers))]

# Plot the bar chart
plt.bar(range(1, len(deltas) + 1), deltas, width=1.0)
plt.xlabel('Index')
plt.ylabel('Delta')
plt.title('Delta Values Between Consecutive Primender Numbers')
plt.tight_layout()
plt.show()
