def filter_chars_by_ascii(x=1, flag=True, *strings):
    # Creeaza o lista goala pentru rezultatul final
    result = []

    # Parcurge fiecare sir primit ca parametru
    for text in strings:
        # Selecteaza caracterele in functie de conditia ceruta
        filtered = []
        for char in text:
            ascii_code = ord(char)
            if flag:
                if ascii_code % x == 0:
                    filtered.append(char)
            else:
                if ascii_code % x != 0:
                    filtered.append(char)

        result.append(filtered)

    return result


# Exemplu de utilizare
print(filter_chars_by_ascii(2, False, "test", "hello", "lab002"))
