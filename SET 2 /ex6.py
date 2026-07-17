def elements_with_exact_count(x, *lists):
    # Creeaza un dictionar pentru a numara aparitiile elementelor
    counts = {}

    # Parcurge fiecare lista
    for lst in lists:
        # Parcurge fiecare element din lista
        for element in lst:
            # Incrementa numarul de aparitii pentru element
            counts[element] = counts.get(element, 0) + 1

    # Selecteaza elementele care apar de exact x ori
    result = [element for element, count in counts.items() if count == x]

    return result


# Exemplu de utilizare
print(elements_with_exact_count(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [7, 1, "test"]))
