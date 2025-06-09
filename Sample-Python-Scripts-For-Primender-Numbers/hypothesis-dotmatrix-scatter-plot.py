import matplotlib.pyplot as plt
from sympy import isprime, prevprime

# Function to generate the Primender sequence
def generate_primender_sequence(n):
    primender_sequence = []
    for i in range(1, n + 1):
        if isprime(i) or i % 10 in {2, 3, 5, 7} or isprime(i % 100) or isprime(i % 1000):
            primender_sequence.append(i)
    return primender_sequence

# Generate the first 100 Primender numbers
primender_numbers = generate_primender_sequence(1000)[:100]

# Calculate delta values (difference between consecutive Primender numbers)
delta_values = [primender_numbers[i] - primender_numbers[i - 1] for i in range(1, len(primender_numbers))]

# Calculate LPn values (largest prime ≤ PEn if prime, otherwise largest prime < PEn)
lp_values = [num if isprime(num) else prevprime(num) for num in primender_numbers]

# Calculate PEn - LPn values
pen_lpn_values = [primender_numbers[i] - lp_values[i] for i in range(len(primender_numbers))]

# Adjust lists for plotting (exclude first delta)
primender_numbers_plot = primender_numbers[1:]
delta_values_plot = delta_values
pen_lpn_values_plot = pen_lpn_values[1:]

# Create Dot Matrix Timeline
plt.figure(figsize=(12, 6))

# Plot Delta values as blue dots
plt.scatter(range(2, len(delta_values_plot) + 2), delta_values_plot, color='blue', s=100, label='Delta values')

# Plot PEn - LPn values as orange dots
plt.scatter(range(2, len(pen_lpn_values_plot) + 2), pen_lpn_values_plot, color='orange', s=50, label='PEn - LPn values')

# Highlight points where both values are 1 with blue rings around orange dots
for i in range(len(delta_values_plot)):
    if delta_values_plot[i] == 1 and pen_lpn_values_plot[i] == 1:
        plt.scatter(i + 2, pen_lpn_values_plot[i], facecolors='none', edgecolors='blue', s=200, linewidths=2)

# Set axis labels and title
plt.xlabel('Primender Index')
plt.ylabel('Values')
plt.title('Dot Matrix Timeline of Delta and PEn - LPn Values for Primender Sequence')
plt.legend()
plt.grid(True)
plt.show()
