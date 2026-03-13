# NWD algorytmem Euklidesa
def nwd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

print(nwd(48, 18))  # 6
print(nwd("a", "a"))  # 6


# NWW
def nww(a: int, b: int) -> int:
    return a * b // nwd(a, b)

print(nww(4, 6))    # 12

# Silnia iteracyjna
def silnia(n: int) -> int:
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

print(silnia(10))   # 3628800

# Cyfry sumy cyfr
def suma_cyfr(n: int) -> int:
    return sum(int(c) for c in str(abs(n)))

print(suma_cyfr(12345))   # 15