def is_palindrome(number):
    # Converteste numarul la sir de caractere
    text = str(number)
    # Verifica daca sirul este identic in ambele parti
    return text == text[::-1]


def even_digit_palindromes(numbers):
    # Creeaza o lista goala pentru rezultatul final
    result = []

    # Parcurge fiecare numar din lista
    for number in numbers:
        # Verifica daca numarul este palindrom si are un numar par de cifre
        if is_palindrome(number) and len(str(number)) % 2 == 0:
            result.append(number)

    return result


# Exemplu de utilizare
print(even_digit_palindromes([11, 22, 121, 12321, 1001, 10001]))
