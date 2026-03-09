"""
Pomocnik API Helper (inspirowany Dive Into Python).
Demonstruje potęgę introspekcji dynamicznego języka.
"""


def pomoc(obj, spacing=15, collapse=True):
    """Wypisuje metody obiektu w sformatowanej tabeli.

    Args:
        obj: Obiekt do zbadania.
        spacing (int): Szerokość kolumny nazwy metody.
        collapse (bool): Czy ucinać/zwijać docstringi do jednej linii.
    """
    # 1. Pobieramy listę metod (callable attributes)
    metody_all = [(attr, getattr(obj, attr)) for attr in dir(obj)]
    metody = [
        (nazwa, metoda)
        for nazwa, metoda in metody_all
        if callable(metoda) and not nazwa.startswith("__")
    ]

    # 2. Funkcja przetwarzająca docstring (lambda condition) (closure)
    process_doc = (
        (lambda s: " ".join(s.split())) if collapse else (lambda s: s)
    )

    print(f"\nObiekt typu: {type(obj).__name__}")
    print("-" * (spacing + 40))

    for nazwa, metoda in metody:
        doc = str(metoda.__doc__) if metoda.__doc__ else "(brak dokumentacji)"
        # Aplikujemy funkcję przetwarzającą
        doc_processed = process_doc(doc)

        # Przycinamy, żeby nie było za długie w konsoli
        if len(doc_processed) > 60:
            doc_processed = doc_processed[:57] + "..."

        print(f"{nazwa.ljust(spacing)} {doc_processed}")
    print("-" * (spacing + 40))


if __name__ == "__main__":
    lista = []
    pomoc(lista)

    napis = "Python"
    pomoc(napis, collapse=False)

