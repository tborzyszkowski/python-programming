"""Symulacja Deterministycznego Automatu Skonczonego (DFA) w Pythonie.

Pokazuje, jak dziala dopasowywanie wzorca na poziomie teorii automatow –
krok po kroku ze sledzeniem sciezki stanow.

Uruchomienie:
    python src/_06-regex/01-formal-languages/examples/dfa_simulator.py
"""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class DFA:
    """Deterministyczny Automat Skonczony.

    Attributes:
        stany: Zbior wszystkich stanow.
        alfabet: Zbior dopuszczalnych symboli.
        przejscia: Slownik {(stan, symbol): nowy_stan}.
        start: Stan poczatkowy.
        akceptujace: Zbior stanow akceptujacych.
    """

    stany: set[str]
    alfabet: set[str]
    przejscia: dict[tuple[str, str], str]
    start: str
    akceptujace: set[str]

    def akceptuje(self, slowo: str) -> bool:
        """Zwraca True, jesli automat akceptuje dane slowo."""
        stan = self.start
        for symbol in slowo:
            if symbol not in self.alfabet:
                return False
            klucz = (stan, symbol)
            if klucz not in self.przejscia:
                return False
            stan = self.przejscia[klucz]
        return stan in self.akceptujace

    def trace(self, slowo: str) -> list[str]:
        """Zwraca sciezke stanow (wlacznie ze stanem poczatkowym)."""
        sciezka = [self.start]
        stan = self.start
        for symbol in slowo:
            if symbol not in self.alfabet:
                sciezka.append("DEAD")
                return sciezka
            klucz = (stan, symbol)
            if klucz not in self.przejscia:
                sciezka.append("DEAD")
                return sciezka
            stan = self.przejscia[klucz]
            sciezka.append(stan)
        return sciezka

    def opisz(self, slowo: str) -> None:
        """Wypisuje szczegolowy opis przetwarzania slowa."""
        print(f"\nSlowo: {slowo!r}")
        sciezka = self.trace(slowo)
        for i, (sym, stan) in enumerate(zip(slowo, sciezka[1:])):
            prev = sciezka[i]
            marker = " *" if stan in self.akceptujace else ""
            print(f"  {prev!r} --[{sym}]--> {stan!r}{marker}")
        wynik = self.akceptuje(slowo)
        print(f"  Wynik: {'AKCEPTUJE ✓' if wynik else 'ODRZUCA ✗'}")


# ---- Przyklad 1: DFA rozpoznajacy napisy konczace sie na "ab" ----

DFA_KONCZY_AB = DFA(
    stany={"q0", "q1", "q2"},
    alfabet={"a", "b"},
    przejscia={
        ("q0", "a"): "q1",
        ("q0", "b"): "q0",
        ("q1", "a"): "q1",
        ("q1", "b"): "q2",
        ("q2", "a"): "q1",
        ("q2", "b"): "q0",
    },
    start="q0",
    akceptujace={"q2"},
)

# ---- Przyklad 2: DFA rozpoznajacy ciagi binarne parzyste ----
# Jezyk: ciagi nad {0,1}, ktore interpretowane binarnie sa parzyste
# (ostatnia cyfra to 0)

DFA_BINARNE_PARZYSTE = DFA(
    stany={"par", "nieparz"},
    alfabet={"0", "1"},
    przejscia={
        ("par", "0"): "par",
        ("par", "1"): "nieparz",
        ("nieparz", "0"): "par",
        ("nieparz", "1"): "nieparz",
    },
    start="par",
    akceptujace={"par"},
)

# ---- Przyklad 3: DFA rozpoznajacy identyfikatory (litera, potem litery/cyfry) ----

LITERY = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
CYFRY = set("0123456789")
ALFABET_ID = LITERY | CYFRY

przejscia_id: dict[tuple[str, str], str] = {}
for c in LITERY:
    przejscia_id[("start", c)] = "ok"
    przejscia_id[("ok", c)] = "ok"
for c in CYFRY:
    przejscia_id[("ok", c)] = "ok"
    przejscia_id[("start", c)] = "dead"

DFA_IDENTYFIKATOR = DFA(
    stany={"start", "ok", "dead"},
    alfabet=ALFABET_ID,
    przejscia=przejscia_id,
    start="start",
    akceptujace={"ok"},
)


if __name__ == "__main__":
    print("=" * 50)
    print("DFA 1: Napisy konczace sie na 'ab'")
    print("=" * 50)
    for slowo in ["ab", "aab", "bab", "ba", "b", "", "ababab"]:
        DFA_KONCZY_AB.opisz(slowo)

    print("\n" + "=" * 50)
    print("DFA 2: Binarne liczby parzyste")
    print("=" * 50)
    for slowo in ["0", "10", "11", "100", "1010", "111", ""]:
        DFA_BINARNE_PARZYSTE.opisz(slowo)

    print("\n" + "=" * 50)
    print("DFA 3: Poprawne identyfikatory")
    print("=" * 50)
    for slowo in ["abc", "a1b2", "1abc", "x", "", "CamelCase"]:
        DFA_IDENTYFIKATOR.opisz(slowo)

