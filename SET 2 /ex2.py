def is_prime(number):
    # Verifica daca numarul este mai mic decat 2
    if number < 2:
        return False

    # Verifica daca numarul este divizibil cu un numar mai mic decat el
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def prime_numbers(numbers):
    # Creeaza o lista goala pentru numerele prime
    result = []

    # Parcurge fiecare numar din lista initiala
    for number in numbers:
        # Adauga numarul in lista daca este prim
        if is_prime(number):
            result.append(number)

    return result


# Exemplu de utilizare
print(prime_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10]))
