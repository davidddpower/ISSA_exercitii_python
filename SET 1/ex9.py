# 9. Write a function that returns the largest prime number from a string
def is_prime(n):
    """Verifică dacă un număr este prim."""
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def find_largest_prime_in_string(s):
    """Extrage cel mai mare număr prim dintr-un string."""
    numbers = re.findall(r'\d+', s)
    primes = [int(num) for num in numbers if is_prime(int(num))]
    return max(primes) if primes else -1
