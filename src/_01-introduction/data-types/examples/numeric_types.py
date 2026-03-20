"""
Demonstracja typów liczbowych w Pythonie 3.
Uruchomienie: python numbers.py
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import cmath
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
    print(f"-17 // 5 = {-17 // 5}  (podłoga, nie obcięcie!)")
    print(f"-17 %  5 = {-17 % 5}  (zawsze nieujemne gdy dzielnik > 0)")
    print(f"2 ** 10 = {2 ** 10}")
    print(f"abs(-5) = {abs(-5)}")
    print(f"divmod(17, 5) = {divmod(17, 5)}")
    print(f"pow(2, 10, 1000) = {pow(2, 10, 1000)}  (szybkie potęgowanie modulo)")

    # Różne systemy zapisu
    print(f"\nLiterały: hex=0xFF → {0xFF}, oct=0o17 → {0o17}, bin=0b1010 → {0b1010}")
    print(f"hex(255) = {hex(255)}, oct(8) = {oct(8)}, bin(10) = {bin(10)}")

    # Porównanie z Python 2
    print(f"\nPython 3 int – nieograniczona precyzja:")
    print(f"  factorial(50) = {math.factorial(50)}")
    print(f"  (2**63).bit_length() = {(2**63).bit_length()} bitów")
    print(f"  (10**100).bit_length() = {(10**100).bit_length()} bitów")


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
    print(f"sys.float_info.epsilon = {sys.float_info.epsilon:.3e}")


def demo_float_epsilon() -> None:
    print("\n" + "=" * 50)
    print("FLOAT – epsilon maszynowy i zakres")
    print("=" * 50)

    print("Informacje o float:")
    print(f"  max         = {sys.float_info.max:.6e}")
    print(f"  min (norm.) = {sys.float_info.min:.6e}")
    print(f"  epsilon     = {sys.float_info.epsilon:.6e}")
    print(f"  dig (cyfry) = {sys.float_info.dig}")

    # Wyznaczenie epsilon ręcznie
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps /= 2
    eps *= 2
    print(f"\nEpsilon wyznaczony ręcznie: {eps:.6e}")
    print(f"Zgodny z sys.float_info:    {eps == sys.float_info.epsilon}")

    # Najmniejsza dodatnia liczba (subnormalna)
    x = 1.0
    while x / 2 > 0:
        x /= 2
    print(f"\nNajmniejsza dodatnia float: {x}")
    print(f"float('5e-324') > 0:       {5e-324 > 0}")
    print(f"float('5e-324') / 2 == 0:  {5e-324 / 2 == 0.0}  (underflow)")


def demo_float_algorithms() -> None:
    print("\n" + "=" * 50)
    print("FLOAT – algorytmy numeryczne")
    print("=" * 50)

    # Pierwiastek kwadratowy metodą Newtona
    def pierwiastek_newton(n: float, eps: float = 1e-10) -> float:
        if n < 0:
            raise ValueError("Argument ujemny")
        if n == 0:
            return 0.0
        x = n
        while True:
            nastepny = (x + n / x) / 2
            if abs(x - nastepny) < eps:
                return nastepny
            x = nastepny

    print("Pierwiastek metodą Newtona:")
    for v in [2, 9, 144, 2.0]:
        wynik = pierwiastek_newton(v)
        print(f"  sqrt({v}) = {wynik:.10f}  (math.sqrt = {math.sqrt(v):.10f})")

    # Równanie kwadratowe
    def rowna_kwadratowe(a: float, b: float, c: float) -> tuple:
        delta = b**2 - 4*a*c
        if delta < 0:
            return ()
        if math.isclose(delta, 0):
            return (-b / (2*a),)
        sq = math.sqrt(delta)
        return ((-b - sq) / (2*a), (-b + sq) / (2*a))

    print("\nRównania kwadratowe:")
    for params in [(1, -3, 2), (1, -2, 1), (1, 0, 1), (2, -7, 3)]:
        a, b, c = params
        roots = rowna_kwadratowe(a, b, c)
        print(f"  {a}x²+{b}x+{c}=0 → {roots}")


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
    print(f"cmath.phase(z1) = {cmath.phase(z1):.4f} rad")
    print(f"cmath.polar(z1) = {cmath.polar(z1)}")
    print(f"cmath.sqrt(-1)  = {cmath.sqrt(-1)}")

    # Wzór Eulera
    euler = cmath.exp(1j * math.pi)
    print(f"\nWzór Eulera e^(iπ) = {euler}")
    print(f"≈ -1? isclose = {cmath.isclose(euler, -1)}")

    # Obrót punktu w 2D
    print("\nObrót punktu (1, 0) o wielokrotności 60°:")
    for k in range(6):
        p = cmath.exp(1j * 2 * math.pi * k / 6)
        print(f"  {k*60:3d}°: ({p.real:+.3f}, {p.imag:+.3f})")


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
    demo_float_epsilon()
    demo_float_algorithms()
    demo_decimal()
    demo_complex()
    demo_fraction()



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

