a = 0.1 + 0.2
b = 0.3
print(a == b)          # False (!)
print(abs(a - b))      # 5.551115123125783e-17

# Poprawne podejście – porównanie z tolerancją
import math

# Tolerancja absolutna (dla wartości bliskich 0)
print(abs(a - b) < 1e-9)          # True

# Tolerancja względna + absolutna (math.isclose)
print(math.isclose(a, b))                     # True (domyślnie rel_tol=1e-09)
print(math.isclose(a, b, rel_tol=1e-9))       # True
print(math.isclose(1e10, 1e10 + 1, rel_tol=1e-9))  # True  (~ 0 względnie)
print(math.isclose(0.0, 1e-15, abs_tol=1e-9))      # True  (bliskie zera)

# Specjalne wartości
print(math.isinf(float('inf')))    # True
print(math.isnan(float('nan')))    # True
print(float('nan') == float('nan'))  # False  (NaN != NaN!)