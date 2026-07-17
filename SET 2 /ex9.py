def sort_tuples_by_third_char(items):
    # Sorteaza tuplurile in functie de al treilea caracter al celui de-al doilea element
    return sorted(items, key=lambda item: item[1][2])


# Exemplu de utilizare
print(sort_tuples_by_third_char([('abc', 'bcd'), ('abc', 'zza')]))
