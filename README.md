# Primender Sequence

The **Primender Sequence** is a novel mathematical construct that includes numbers which are **prime**, or which **end with a prime number** (of any length). In simpler terms, a number qualifies as a Primender if it:

- Is a prime number itself, **or**
- Has at least one **suffix** (ending segment) that is a prime number.

For example:
- `2`, `3`, `5`, `7` → Prime numbers → ✅
- `12` → Ends in `2` (a prime) → ✅
- `12345699` → Ends with suffix `45699` (a prime) → ✅

### Properties

- The sequence is **infinite**.
- It is **densely populated**, with the **maximum delta (difference) between consecutive terms never exceeding 5**.
- **All prime numbers** are included in the Primender sequence.
- The rule-based structure offers a **symbolic and computational framework** to analyze **prime distribution, modular arithmetic, and AI inference patterns**.

### Applications

This sequence opens avenues for:
- Symbolic reasoning tasks
- Cryptographic keyspace exploration
- Pseudo-random number generation
- Benchmarking interpretable AI systems and LLM inference consistency

### Sample Python Implementation

```python
from sympy import isprime

def is_primender(n):
    s = str(n)
    return any(isprime(int(s[i:])) for i in range(len(s)))

# Generate first 1000 Primender numbers
primender_numbers = []
n = 1

while len(primender_numbers) < 1000:
    if is_primender(n):
        primender_numbers.append(n)
    n += 1

print("First 1000 Primender numbers:", primender_numbers)
