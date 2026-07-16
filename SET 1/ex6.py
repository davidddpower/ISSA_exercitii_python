# 6. Write a function that converts a string of characters written in UpperCamelCase into snake_case
def camel_to_snake(s):
    """Convertește UpperCamelCase în snake_case."""
    # Adaugă un underscore înainte de fiecare literă mare, apoi pune totul în minusculă
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
