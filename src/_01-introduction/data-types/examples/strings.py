"""
Demonstracja napisów (str) w Pythonie 3.
Uruchomienie: python strings.py
"""


def demo_tworzenie() -> None:
    print("=" * 50)
    print("Tworzenie napisów")
    print("=" * 50)
    s1 = 'Pojedyncze apostrofy'
    s2 = "Podwójne cudzysłowy"
    s3 = """Tekst
wieloliniowy"""
    raw = r"C:\nowy\folder\test"    # r-string: backslash nie jest znakiem ucieczki
    bajty = b"dane binarne"

    print(repr(s1))
    print(repr(s2))
    print(repr(s3))
    print(f"raw string: {raw}")
    print(f"bytes: {bajty}, type: {type(bajty)}")


def demo_operacje() -> None:
    print("\n" + "=" * 50)
    print("Operacje na napisach")
    print("=" * 50)

    s = "Python"
    print(f"s = {repr(s)}")
    print(f"len(s)       = {len(s)}")
    print(f"s[0]         = {s[0]!r}")       # 'P'
    print(f"s[-1]        = {s[-1]!r}")      # 'n'
    print(f"s[1:4]       = {s[1:4]!r}")    # 'yth'
    print(f"s[::2]       = {s[::2]!r}")    # 'Pto'
    print(f"s[::-1]      = {s[::-1]!r}")   # 'nohtyP'
    print(f"s + ' 3'     = {s + ' 3'!r}")
    print(f"'ha' * 3     = {'ha' * 3!r}")
    print(f"'yt' in s    = {'yt' in s}")


def demo_metody() -> None:
    print("\n" + "=" * 50)
    print("Metody napisów")
    print("=" * 50)

    s = "  Python 3 jest super!  "
    print(f"strip()    = {s.strip()!r}")
    print(f"lstrip()   = {s.lstrip()!r}")
    print(f"upper()    = {s.upper()!r}")
    print(f"lower()    = {s.lower()!r}")
    print(f"title()    = {'hello world'.title()!r}")
    print(f"split()    = {s.split()}")
    print(f"replace()  = {s.replace('super', 'świetny')!r}")
    print(f"find('3')  = {s.find('3')}")
    print(f"count('y') = {'Python'.count('y')}")
    print(f"startswith = {'Python'.startswith('Py')}")
    print(f"endswith   = {'Python'.endswith('on')}")
    print(f"join       = {', '.join(['a', 'b', 'c'])!r}")
    print(f"zfill(5)   = {'42'.zfill(5)!r}")
    print(f"center(10) = {'hi'.center(10, '-')!r}")


def demo_formatowanie() -> None:
    print("\n" + "=" * 50)
    print("Formatowanie napisów")
    print("=" * 50)

    imie = "Anna"
    wiek  = 30
    pi    = 3.14159265

    # f-string
    print(f"f-string:   Witaj, {imie}! Masz {wiek} lat.")
    print(f"float 2dp:  pi ≈ {pi:.2f}")
    print(f"notacja e:  pi = {pi:.4e}")
    print(f"hex:        255 = {255:#010x}")
    print(f"bin:        10  = {10:#010b}")
    print(f"% szerok.:  |{'test':>10}|  |{'test':<10}|  |{'test':^10}|")

    # format()
    wzorzec = "Witaj, {imie}! Masz {wiek} lat."
    print(wzorzec.format(imie=imie, wiek=wiek))

    # = w f-string (Python 3.8+) – debug
    x = 42
    print(f"debug: {x = }")


if __name__ == "__main__":
    demo_tworzenie()
    demo_operacje()
    demo_metody()
    demo_formatowanie()

