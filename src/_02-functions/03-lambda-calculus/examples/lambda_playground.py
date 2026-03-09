"""Większy przykład: composable lambdy na danych liczbowych."""


def compose(f, g):
    return lambda x: f(g(x))


def make_pipeline(*funcs):
    """Składa wiele funkcji w jedną pipeline'ową funkcję."""
    if not funcs:
        return lambda x: x

    def pipeline(x):
        for f in funcs:
            x = f(x)
        return x

    return pipeline


if __name__ == "__main__":
    # Pojedyncze lambdy
    add1 = lambda x: x + 1
    square = lambda x: x * x
    half = lambda x: x / 2

    # Kompozycja f(g(x))
    h = compose(square, add1)  # (x+1)^2
    print("compose square(add1(x)) dla x=3 ->", h(3))

    # Pipeline wielu kroków
    p = make_pipeline(add1, square, half)
    print("pipeline add1 -> square -> half dla x=3 ->", p(3))

    dane = [1, 2, 3, 4, 5]
    transform = make_pipeline(lambda x: x * 3, lambda x: x - 1)
    wynik = [transform(x) for x in dane]
    print("transformacja listy:", wynik)

