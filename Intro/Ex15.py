def sorted_main_diagonal(matrix):
    # Extrage elementele diagonalei principale
    diagonal = [matrix[i][i] for i in range(len(matrix))]

    # Sorteaza diagonalul in ordine descrescatoare
    diagonal.sort(reverse=True)

    return diagonal


# Exemplu de utilizare
print(sorted_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
