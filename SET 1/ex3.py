# 3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string
import re
def count_words(s):
    """Numără cuvintele dintr-un string, separând prin spații sau semne de punctuație."""
    # Split by any sequence of spaces or punctuation characters
    words = re.split(r'[\s,;?!.]+', s)
    # Filtram pentru a elimina șirurile vide rezultate din split
    return len([w for w in words if w])
