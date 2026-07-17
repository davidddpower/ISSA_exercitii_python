def fibonacci_sequence(n):
    # Verifica daca numarul de termeni este invalid
    if n <= 0:
        return []

    # Creeaza lista cu primii doi termeni ai sirului
    sequence = [0, 1]

    # Genereaza restul termenilor
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]


def generalized_fibonacci(num_terms, n):
    # Verifica daca numarul de termeni este invalid
    if num_terms <= 0 or n <= 0:
        return []

    # Initializeaza sirul cu n-1 zerouri si un 1
    sequence = [0] * (n - 1) + [1]

    # Genereaza termenii urmatori
    while len(sequence) < num_terms:
        next_term = sum(sequence[-n:])
        sequence.append(next_term)

    return sequence[:num_terms]


# Exemplu de utilizare
print(fibonacci_sequence(10))
print(generalized_fibonacci(10, 5))
