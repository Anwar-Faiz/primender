def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

sequence = []
n = 186
while len(sequence) < 100000:
    if is_prime(n) or is_prime(n - 1):
        sequence.append(n)
    n += 1

with open("Output/grok-3/grok-3-generated-100000-terms--.txt", "w") as f:
    for num in sequence:
        f.write(f"{num}\n")