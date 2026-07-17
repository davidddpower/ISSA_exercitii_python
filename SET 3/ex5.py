def validate_dict(rules, data):
    # Verifica daca dictionarul contine doar chei permise
    if set(data.keys()) - {rule[0] for rule in rules}:
        return False

    # Verifica fiecare regula
    for key, prefix, middle, suffix in rules:
        if key not in data:
            continue

        value = data[key]

        # Verifica prefixul
        if not value.startswith(prefix):
            return False

        # Verifica faptul ca middle este in interiorul sirului
        if not (len(middle) == 0 or (len(value) > len(middle) and middle in value[1:-1])):
            return False

        # Verifica sufixul
        if not value.endswith(suffix):
            return False

    return True


# Exemplu de utilizare
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside", "key3": "this is not valid"}
print(validate_dict(rules, data))
