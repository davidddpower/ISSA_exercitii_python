# 2. Write a function that calculates how many vowels are in a string
def count_vowels(s):
    """Numără vocalele dintr-un string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
