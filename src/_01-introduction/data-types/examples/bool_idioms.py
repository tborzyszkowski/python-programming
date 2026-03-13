# Wartość domyślna gdy None lub falsy
def pobierz_imie(dane: dict) -> str:
    return dane.get("imie") or "Anonim"

print(pobierz_imie({"imie": "Ania"}))  # "Ania"
print(pobierz_imie({}))                # "Anonim"
# Uwaga: puste "" też da "Anonim" – czy to pożądane?

# Bezpieczniejsze – tylko None pomijamy:
def pobierz_imie_v2(dane: dict) -> str:
    wartosc = dane.get("imie")
    return wartosc if wartosc is not None else "Anonim"

# Leniwa inicjalizacja – otwieraj plik tylko jeśli istnieje
import os
plik = "config.txt"
zawartosc = os.path.exists(plik) and open(plik).read()