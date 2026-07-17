def combinations(lst, k):
    # Verifica daca k este valid
    if k < 0 or k > len(lst):
        return []

    # Daca k este 0, returneaza o combinatie goala
    if k == 0:
        return [()]

    # Genereaza combinatiile recursive
    if len(lst) == k:
        return [tuple(lst)]

    first = lst[0]
    rest = lst[1:]

    # Combinatiile care contin primul element
    with_first = [(first,) + combo for combo in combinations(rest, k - 1)]

    # Combinatiile care nu contin primul element
    without_first = combinations(rest, k)

    return with_first + without_first


# Exemplu de utilizare
print(combinations([1, 2, 3, 4], 3))
