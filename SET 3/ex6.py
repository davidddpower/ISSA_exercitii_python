# 6 Operatori
ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}

def apply_operator(op, a, b):
    return ops[op](a, b)

def apply_function(op_name, *args, **kwargs):
    # Dictionar global de functii
    return globals()[op_name](*args, **kwargs)
