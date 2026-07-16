def sublist_between_min_and_max(numbers):
    # Verifica daca lista are cel putin doua elemente
    if len(numbers) < 2:
        return []

    # Gaseste valoarea minima si maxima
    smallest = min(numbers)
    largest = max(numbers)

    # Gaseste pozitiile lor in lista
    min_index = numbers.index(smallest)
    max_index = numbers.index(largest)

    # Determina inceputul si sfarsitul sublistei
    start = min(min_index, max_index)
    end = max(min_index, max_index) + 1

    # Returneaza sublista dintre cele doua pozitii
    return numbers[start:end]


# Exemplu de utilizare
print(sublist_between_min_and_max([4, 7, 2, 9, 5, 1]))
