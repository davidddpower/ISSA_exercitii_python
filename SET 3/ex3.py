def compare_dictionaries(first, second):
    # Creeaza listele pentru diferentele dorite
    common_with_different_values = []
    only_in_first = []
    only_in_second = []

    # Verifica cheile din primul dictionar
    for key in first:
        if key not in second:
            only_in_first.append(key)
            continue

        first_value = first[key]
        second_value = second[key]

        # Compara valorile recursiv pentru tipuri de date complexe
        if is_primitive(first_value) and is_primitive(second_value):
            if first_value != second_value:
                common_with_different_values.append(key)
        else:
            if not values_equal(first_value, second_value):
                common_with_different_values.append(key)

    # Verifica cheile din al doilea dictionar
    for key in second:
        if key not in first:
            only_in_second.append(key)

    return common_with_different_values, only_in_first, only_in_second


def is_primitive(value):
    # Verifica daca valoarea este un tip primitiv
    return isinstance(value, (int, float, str, bool, type(None)))


def values_equal(first, second):
    # Verifica daca doua valori sunt egale, recursiv
    if is_primitive(first) and is_primitive(second):
        return first == second

    if isinstance(first, dict) and isinstance(second, dict):
        if set(first.keys()) != set(second.keys()):
            return False
        for key in first:
            if not values_equal(first[key], second[key]):
                return False
        return True

    if isinstance(first, (list, tuple)) and isinstance(second, (list, tuple)):
        if len(first) != len(second):
            return False
        for item1, item2 in zip(first, second):
            if not values_equal(item1, item2):
                return False
        return True

    if isinstance(first, set) and isinstance(second, set):
        if len(first) != len(second):
            return False
        return all(value in second for value in first)

    return first == second


# Exemplu de utilizare
print(compare_dictionaries({'a': 1, 'b': {'x': 1, 'y': 2}}, {'a': 2, 'b': {'x': 1, 'y': 3}, 'c': 4}))
