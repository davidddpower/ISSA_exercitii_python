def zip_like(*lists):
    # Determina numarul maxim de elemente dintre liste
    max_length = max(len(lst) for lst in lists) if lists else 0

    # Creeaza o lista de tuple pentru fiecare pozitie
    result = []
    for index in range(max_length):
        tuple_items = []
        for lst in lists:
            # Adauga elementul de pe pozitia curenta sau None daca nu exista
            if index < len(lst):
                tuple_items.append(lst[index])
            else:
                tuple_items.append(None)
        result.append(tuple(tuple_items))

    return result


# Exemplu de utilizare
print(zip_like([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
