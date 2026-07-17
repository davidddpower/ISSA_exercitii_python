def set_operations(a, b):
    # Creeaza seturile pentru operatiile cerute
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    difference_a_b = set(a) - set(b)
    difference_b_a = set(b) - set(a)

    return intersection, union, difference_a_b, difference_b_a


# Exemplu de utilizare
print(set_operations([1, 2, 2, 3], [2, 3, 4]))
