def calculate(x, y, op):
    # Verifica operatorul introdus
    if op == "+":
        return x + y
    # Verifica daca operatorul este scaderea
    elif op == "-":
        return x - y
    # Verifica daca operatorul este inmultirea
    elif op == "*":
        return x * y
    # Verifica daca operatorul este impartirea
    elif op == "/":
        return x / y
    # Daca operatorul nu este valid, returneaza un mesaj
    else:
        return "Operator invalid"

# Exemplu de utilizare
print(calculate(5, 3, "+"))
