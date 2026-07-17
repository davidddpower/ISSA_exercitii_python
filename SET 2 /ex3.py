from math import gcd
def unique_lines(points):
    # Verifica daca lista are mai putin de 2 puncte
    if len(points) < 2:
        return []

    # Creeaza un set pentru a pastra liniile unice
    lines = set()

    # Parcurge toate perechile de puncte
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Ignora punctele identice
            if (x1, y1) == (x2, y2):
                continue

            # Calculeaza coeficientii dreptei ax + by + c = 0
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1

            # Normalizeaza coeficientii pentru a identifica aceeasi dreapta
            g = gcd(abs(a), gcd(abs(b), abs(c)))
            if g != 0:
                a //= g
                b //= g
                c //= g

            # Pastreaza un semn consistent pentru coeficienti
            if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
                a, b, c = -a, -b, -c

            lines.add((a, b, c))

    return sorted(lines)


# Exemplu de utilizare
print(unique_lines([(0, 0), (1, 1), (2, 2), (0, 1), (1, 0)]))
