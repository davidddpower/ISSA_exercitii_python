def is_palindrome(number):
    # Converteste numarul la sir de caractere
    text = str(number)
    # Verifica daca sirul este identic in ambele parti
    return text == text[::-1]

# Exemplu de utilizare
print(is_palindrome(121))
