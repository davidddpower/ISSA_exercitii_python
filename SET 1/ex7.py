# 7. Write a function that checks neighboring strings follow the rule
def check_pheasant_rule(char_len, *args):
    """Verifică dacă fiecare pereche de string-uri consecutive respectă regula pheasant."""
    for i in range(len(args) - 1):
        s1 = args[i]
        s2 = args[i+1]
        if len(s1) < char_len or not s2.startswith(s1[-char_len:]):
            return False
    return True
