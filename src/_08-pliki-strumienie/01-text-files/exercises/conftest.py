import sys
from pathlib import Path
# Usuń poprzednio zaladowany modul 'solutions' z cache Pythona,
# zeby kolejny temat zaladowal SWOJ plik solutions.py.
sys.modules.pop('solutions', None)
# Wstaw lokalny katalog exercises/ na poczatek sys.path.
_here = str(Path(__file__).parent)
if _here not in sys.path:
    sys.path.insert(0, _here)
else:
    # Przesun na poczatek, jesli juz jest
    sys.path.remove(_here)
    sys.path.insert(0, _here)
