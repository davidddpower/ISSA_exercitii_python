# 8. Evaluate the polynomial for the given value
def evaluate_polynomial(poly_str, x):
    """Evaluează un polinom dat ca string pentru o valoare x."""
    # Înlocuim '^' cu '**' pentru Python și asigurăm formatul pentru evaluare
    clean_poly = poly_str.replace('^', '**')
    # Atenție: eval() poate fi periculos cu input-uri nesigure
    return eval(clean_poly, {"x": x})
