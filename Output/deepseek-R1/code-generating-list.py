import math

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_square_free(n):
    """Check if a number is square-free"""
    # Quick checks for small squares
    if n % 4 == 0 or n % 9 == 0 or n % 25 == 0:
        return False
    
    # Check all squares up to sqrt(n)
    f = 2
    while f * f <= n:
        if n % (f * f) == 0:
            return False
        f += 1
    return True

def in_sequence(n):
    """Determine if a number belongs to the Primender sequence"""
    # Special case: 15 is always included
    if n == 15:
        return True
    
    # All primes are included
    if is_prime(n):
        return True
    
    # Non-square-free composites are included
    if not is_square_free(n):
        return True
    
    # For square-free composites: include if any factor > 5
    temp = n
    found_large_factor = False
    for p in [2, 3, 5]:
        while temp % p == 0:
            temp //= p
    if temp > 1:  # Remaining factor must be > 5
        return True
    return False

def generate_sequence(start, count, filename):
    """Generate the sequence and save to file"""
    n = start
    terms = []
    while len(terms) < count:
        if in_sequence(n):
            terms.append(n)
        n += 1
    
    with open(filename, 'w') as f:
        for term in terms:
            f.write(f"{term}\n")
    return terms

# Generate next 100,000 terms after last given term (185)
generate_sequence(1, 100000, "Output/deepseek-R1/primender_sequence_terms_to_100001.txt")