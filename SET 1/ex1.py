# 1. Find the largest common divisor of multiple numbers
def find_gcd(*args):
    """Calculează cel mai mare divizor comun pentru un număr variabil de argumente."""
    if not args:
        return 0
    return math.gcd(*args)
