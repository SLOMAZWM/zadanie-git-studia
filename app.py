def pomnoz(a, b):
    # Mnozenie liczb - polaczenie wersji main i feature-marcin
    if b == 0:
        return 0
    return a * b


def dziel(a, b):
    if b == 0:
        raise ValueError("Nie mozna dzielic przez zero")
    return a / b
