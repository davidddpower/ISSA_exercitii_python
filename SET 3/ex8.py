def count_unique_and_duplicates(values):
    # Creeaza o lista cu elementele din set
    items = list(values)

    # Calculeaza numarul de elemente unice si duplicate
    unique_count = len(items)
    duplicate_count = 0

    # Verifica fiecare element pentru a determina daca este duplicat
    for item in items:
        if items.count(item) > 1:
            duplicate_count += 1

    return unique_count, duplicate_count


# Exemplu de utilizare
print(count_unique_and_duplicates({1, 2, 2, 3, 3, 4}))
