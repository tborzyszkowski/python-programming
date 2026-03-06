"""
Demonstracja typów liczbowych w Pythonie 3.
Uruchomienie: python numbers.py
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import sys


def demo_int() -> None:
    print("=" * 50)
    print("INT – liczby całkowite (nieograniczona precyzja)")
    print("=" * 50)

    a = 42
    b = -17
    duza = 10 ** 100  # googol

    print(f"a = {a}, type = {type(a)}")
    print(f"b = {b}")
    print(f"10^100 = {duza}")
    print(f"17 // 5 = {17 // 5}  (dzielenie całkowite)")
    print(f"17 %  5 = {17 % 5}  (modulo)")
    print(f"2 ** 10 = {2 ** 10}")
    print(f"abs(-5) = {abs(-5)}")

    # Różne systemy zapisu
    print(f"\nLiterały: hex=0xFF → {0xFF}, oct=0o17 → {0o17}, bin=0b1010 → {0b1010}")
    print(f"hex(255) = {hex(255)}, oct(8) = {oct(8)}, bin(10) = {bin(10)}")


def demo_float() -> None:
    print("\n" + "=" * 50)
    print("FLOAT – liczby zmiennoprzecinkowe (IEEE 754)")
    print("=" * 50)

    pi = 3.14159
    e  = 2.71828

    print(f"pi = {pi}, e = {e}")
    print(f"0.1 + 0.2 = {0.1 + 0.2}  (!) – błąd reprezentacji binarnej")
    print(f"round(0.1 + 0.2, 10) = {round(0.1 + 0.2, 10)}")
    print(f"math.isclose(0.1+0.2, 0.3) = {math.isclose(0.1 + 0.2, 0.3)}")

    inf = float('inf')
    nan = float('nan')
    print(f"\ninf = {inf}, -inf = {float('-inf')}")
    print(f"nan = {nan}, math.isnan(nan) = {math.isnan(nan)}")
    print(f"inf > 1e308 = {inf > 1e308}")
    print(f"sys.float_info.max = {sys.float_info.max:.3e}")


def demo_decimal() -> None:
    print("\n" + "=" * 50)
    print("DECIMAL – precyzyjne liczby dziesiętne")
    print("=" * 50)

    getcontext().prec = 28  # domyślna precyzja

    a = Decimal("0.1")
    b = Decimal("0.2")
    print(f"Decimal('0.1') + Decimal('0.2') = {a + b}")  # 0.3 – dokładnie!
    print(f"Decimal('1') / Decimal('3') = {Decimal('1') / Decimal('3')}")


def demo_complex() -> None:
    print("\n" + "=" * 50)
    print("COMPLEX – liczby zespolone")
    print("=" * 50)

    z1 = 3 + 4j
    z2 = complex(1, -2)

    print(f"z1 = {z1}, type = {type(z1)}")
    print(f"z1.real = {z1.real}, z1.imag = {z1.imag}")
    print(f"|z1| = abs(z1) = {abs(z1)}")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1.conjugate() = {z1.conjugate()}")


def demo_fraction() -> None:
    print("\n" + "=" * 50)
    print("FRACTION – ułamki dokładne")
    print("=" * 50)

    f1 = Fraction(1, 3)
    f2 = Fraction(1, 6)
    print(f"1/3 + 1/6 = {f1 + f2}")   # 1/2 – dokładnie!
    print(f"Fraction(0.1) = {Fraction(0.1)}")  # pokazuje problem float


if __name__ == "__main__":
    demo_int()
    demo_float()
    demo_decimal()
    demo_complex()
    demo_fraction()

