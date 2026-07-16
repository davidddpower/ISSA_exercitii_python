import math


def mean_and_geometric_mean(numbers):
    # Verifica daca lista are cel putin un element
    if not numbers:
        return None

    # Gaseste cel mai mic si cel mai mare element
    smallest = min(numbers)
    largest = max(numbers)

    # Calculeaza media aritmetica si media geometrica
    mean = (smallest + largest) / 2
    geometric_mean = math.sqrt(smallest * largest)

    return mean, geometric_mean


# Exemplu de utilizare
print(mean_and_geometric_mean([1, 13, 8]))
