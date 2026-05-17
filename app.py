def pomnoz(a, b):
    # Mnozenie liczb - wersja feature-marcin
    return a * b


def dziel(a, b):
    if b == 0:
        raise ValueError("Nie mozna dzielic przez zero")
    return a / b
