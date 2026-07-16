def largest_first_half_smallest_second_half(numbers):
    # Verifica daca lista are cel putin doua elemente
    if len(numbers) < 2:
        return None

    # Imparte lista in doua jumatati
    first_half = numbers[:len(numbers) // 2]
    second_half = numbers[len(numbers) // 2:]

    # Gaseste cel mai mare element din prima jumatate si cel mai mic din a doua
    largest_first = max(first_half)
    smallest_second = min(second_half)

    return largest_first, smallest_second


# Exemplu de utilizare
print(largest_first_half_smallest_second_half([1, 6, 3, 8, 2, 9]))
