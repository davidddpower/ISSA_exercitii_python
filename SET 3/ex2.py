def count_characters(text):
    # Creeaza un dictionar gol pentru a numara aparitiile
    counts = {}

    # Parcurge fiecare caracter din sir
    for char in text:
        # Incrementa numarul de aparitii pentru caracterul curent
        counts[char] = counts.get(char, 0) + 1

    return counts


def count_characters_manual(text):
    # Creeaza un dictionar gol pentru a numara aparitiile
    counts = {}

    # Parcurge fiecare caracter din sir manual
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


# Exemplu de utilizare
print(count_characters("Ana are mere."))
print(count_characters_manual("Ana are mere."))
