def is_prime(number):
    # Verifica daca numarul este mai mic decat 2
    if number < 2:
        return False

    # Verifica daca numarul este divizibil cu un numar mai mic decat el
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True

# Exemplu de utilizare
print(is_prime(3))
