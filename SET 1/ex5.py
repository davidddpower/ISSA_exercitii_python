# 5. Write a function that checks whether a string contains special characters
def contains_special_chars(s):
    """Verifică dacă un string conține caractere speciale."""
    special_chars = {'\r', '\t', '\n', '\a', '\b', '\f', '\v'}
    return any(char in special_chars for char in s)
