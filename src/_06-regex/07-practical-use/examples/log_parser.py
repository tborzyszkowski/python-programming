"""Parser logow Apache Combined Log Format.

Format linii:
    IP - user [czas] "METODA sciezka protokol" status rozmiar

Uruchomienie:
    python src/_06-regex/07-practical-use/examples/log_parser.py
"""
import re
from typing import Iterator

LOG_RE = re.compile(r"""
    ^
    (\S+)               # 1: IP klienta
    \s+\S+\s+           # ident i identyfikator (pomijamy)
    (\S+)               # 2: uzytkownik auth (- jesli brak)
    \s+\[([^\]]+)\]     # 3: czas w nawiasach kwadratowych
    \s+"                # otwarcie cudzyslowu
    (\S+)               # 4: metoda HTTP
    \s+(\S+)            # 5: sciezka URL
    \s+(\S+)"           # 6: protokol
    \s+(\d{3})          # 7: kod statusu HTTP
    \s+(\d+|-)          # 8: rozmiar odpowiedzi (- jezeli 0)
    $
""", re.VERBOSE)

PRZYKLADOWE_LOGI = [
    '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 1234',
    '192.168.1.10 - - [15/Mar/2024:08:30:00 +0100] "POST /api/login HTTP/1.1" 401 89',
    '10.0.0.1 - admin [01/Jan/2025:00:00:01 +0000] "DELETE /resource/42 HTTP/2" 204 -',
    'USZKODZONA LINIA BEZ FORMATU',
]


def parsuj_linie(linia: str) -> dict | None:
    """Parsuje pojedyncza linie logu Apache. Zwraca slownik lub None."""
    m = LOG_RE.match(linia.strip())
    if not m:
        return None
    return {
        'ip':        m.group(1),
        'uzytkownik': m.group(2),
        'czas':      m.group(3),
        'metoda':    m.group(4),
        'sciezka':   m.group(5),
        'protokol':  m.group(6),
        'status':    int(m.group(7)),
        'rozmiar':   int(m.group(8)) if m.group(8) != '-' else 0,
    }


def parsuj_logi(linie: list[str]) -> Iterator[dict]:
    """Generator zwracajacy slowniki dla poprawnych linii."""
    for linia in linie:
        wynik = parsuj_linie(linia)
        if wynik:
            yield wynik


if __name__ == "__main__":
    print("=== Parser logow Apache ===\n")
    for linia in PRZYKLADOWE_LOGI:
        wynik = parsuj_linie(linia)
        print(f"Linia: {linia[:60]}...")
        if wynik:
            for k, v in wynik.items():
                print(f"  {k:12s}: {v}")
        else:
            print("  [BLAD: nie mozna sparsowac]")
        print()

    print("=== Statystyki ===")
    rekordy = list(parsuj_logi(PRZYKLADOWE_LOGI))
    print(f"  Sparsowano: {len(rekordy)}/{len(PRZYKLADOWE_LOGI)} linii")
    kody = [r['status'] for r in rekordy]
    print(f"  Kody statusu: {kody}")
    bledy = [r for r in rekordy if r['status'] >= 400]
    print(f"  Bledy (4xx/5xx): {len(bledy)}")

