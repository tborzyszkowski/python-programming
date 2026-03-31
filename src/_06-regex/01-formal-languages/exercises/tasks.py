"""Zadania: jezyki formalne i automaty skonczone.

Uzupelnij implementacje funkcji ponizej.
"""
import re


def czy_zawiera_cyfre(s: str) -> bool:
    """Zwraca True, jesli napis zawiera co najmniej jedna cyfre (0-9).

    Przyklad:
        czy_zawiera_cyfre("abc3")  -> True
        czy_zawiera_cyfre("abc")   -> False
        czy_zawiera_cyfre("")      -> False
    """
    raise NotImplementedError("Zaimplementuj czy_zawiera_cyfre")


def czy_ciag_binarny(s: str) -> bool:
    """Zwraca True, jesli niepusty napis sklada sie wylacznie z '0' i '1'.

    Przyklad:
        czy_ciag_binarny("1010")  -> True
        czy_ciag_binarny("0")     -> True
        czy_ciag_binarny("102")   -> False
        czy_ciag_binarny("")      -> False
    """
    raise NotImplementedError("Zaimplementuj czy_ciag_binarny")


def symuluj_dfa(przejscia: dict, start: str, akceptujace: set, slowo: str) -> bool:
    """Symuluje deterministyczny automat skonczony (DFA).

    Args:
        przejscia: Slownik {(stan, symbol): nowy_stan}.
        start: Stan poczatkowy.
        akceptujace: Zbior stanow akceptujacych.
        slowo: Slowo do sprawdzenia.

    Zwraca True, jesli automat akceptuje slowo, False w przeciwnym razie.
    Jesli symbol nie ma przejscia ze stanu biezacego, automat odrzuca slowo.

    Przyklad:
        # DFA akceptujacy napisy zaczynajace sie od 'a'
        p = {('q0','a'): 'q1', ('q1','a'): 'q1', ('q1','b'): 'q1'}
        symuluj_dfa(p, 'q0', {'q1'}, 'ab')  -> True
        symuluj_dfa(p, 'q0', {'q1'}, 'ba')  -> False
        symuluj_dfa(p, 'q0', {'q1'}, '')    -> False
    """
    raise NotImplementedError("Zaimplementuj symuluj_dfa")


def licz_dopasowania(pattern: str, text: str) -> int:
    """Zwraca liczbe nieprzekrywajacych sie dopasowani wzorca w tekscie.

    Przyklad:
        licz_dopasowania(r'\\d+', 'abc 123 def 456')  -> 2
        licz_dopasowania(r'ab', 'ababab')              -> 3
        licz_dopasowania(r'\\d+', 'brak')              -> 0
    """
    raise NotImplementedError("Zaimplementuj licz_dopasowania")

