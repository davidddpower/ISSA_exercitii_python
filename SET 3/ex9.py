def pairwise_set_operations(*sets):
    # Creeaza un dictionar pentru rezultatele operatiilor
    result = {}

    # Parcurge toate perechile de seturi
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            left = sets[i]
            right = sets[j]

            # Creeaza etichetele pentru fiecare operatie
            left_name = str(left)
            right_name = str(right)

            # Calculeaza rezultatul fiecarei operatii
            result[f"{left_name} | {right_name}"] = len(left | right)
            result[f"{left_name} & {right_name}"] = len(left & right)
            result[f"{left_name} - {right_name}"] = len(left - right)
            result[f"{right_name} - {left_name}"] = len(right - left)

    return result


# Exemplu de utilizare
print(pairwise_set_operations({1, 2}, {2, 3}))
