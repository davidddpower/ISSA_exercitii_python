GLOBAL_FUNCTIONS = {
    "print_all": lambda *args, **kwargs: print(args, kwargs),
    "print_args_commas": lambda *args, **kwargs: print(args, kwargs, sep=", "),
    "print_only_args": lambda *args, **kwargs: print(args),
    "print_only_kwargs": lambda *args, **kwargs: print(kwargs),
}


def apply_function(function_name, *args, **kwargs):
    # Verifica daca functia exista in dictionarul global
    if function_name not in GLOBAL_FUNCTIONS:
        raise ValueError(f"Function '{function_name}' is not defined")

    # Aplica functia corespunzatoare cu argumentele primite
    return GLOBAL_FUNCTIONS[function_name](*args, **kwargs)


# Exemplu de utilizare
apply_function("print_all", 1, 2, 3, name="Alice")
