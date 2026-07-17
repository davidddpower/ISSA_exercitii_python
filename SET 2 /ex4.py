def list_operations(a, b):
    # Creeaza liste goale pentru rezultatele finale
    intersection = []
    union = []
    difference_a_b = []
    difference_b_a = []

    # Adauga elementele din a si b in union, fara duplicate
    for element in a:
        if element not in union:
            union.append(element)

    for element in b:
        if element not in union:
            union.append(element)

    # Calculeaza intersectia
    for element in a:
        if element in b and element not in intersection:
            intersection.append(element)

    # Calculeaza a - b
    for element in a:
        if element not in b and element not in difference_a_b:
            difference_a_b.append(element)

    # Calculeaza b - a
    for element in b:
        if element not in a and element not in difference_b_a:
            difference_b_a.append(element)

    return intersection, union, difference_a_b, difference_b_a


# Exemplu de utilizare
print(list_operations([1, 2, 2, 3], [2, 3, 4]))
