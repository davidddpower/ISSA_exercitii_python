def highest_of_three(a, b, c):
    # Verifica daca primul numar este cel mai mare
    if a >= b and a >= c:
        return a
    # Verifica daca al doilea numar este cel mai mare
    elif b >= a and b >= c:
        return b
    # In caz contrar, al treilea numar este cel mai mare
    else:
        return c

# Exemplu de utilizare
print(highest_of_three(10, 4, 7))
