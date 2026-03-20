# 06 - Separation of Concerns (SoC)
> Cel: pokazac, jak projektowac kod funkcyjny w Pythonie tak, aby byl czytelny, testowalny i odporny na zmiany.
## 1. Kontekst historyczny (Dijkstra) - wybor 1B
Edsger W. Dijkstra podkreslal, ze przy zlozonych problemach trzeba swiadomie oddzielac aspekty, o ktorych myslimy. To podejscie pozwala utrzymac porzadek rozumowania i ograniczyc chaos projektowy.
W programowaniu przeklada sie to na projektowanie granic miedzy czesciami systemu: inna czesc odpowiada za obliczenia, inna za prezentacje, a jeszcze inna za interakcje z uzytkownikiem. Dzieki temu kazdy fragment kodu mozna analizowac i testowac niezaleznie.
To jest praktyczna istota Separation of Concerns: rozdzielac odpowiedzialnosci tak, aby zmiany w jednej warstwie nie wymuszaly zmian wszedzie indziej.
> "The separation of concerns ... is the only available technique for effective ordering of one's thoughts."  
> — Edsger W. Dijkstra
## 2. SoC i SRP
- **SRP**: pojedyncza funkcja ma jeden powod do zmiany.
- **SoC**: caly system ma oddzielone obszary odpowiedzialnosci.
SRP porzadkuje funkcje lokalnie, a SoC porzadkuje architekture globalnie.
## 3. Architektura warstwowa
W tym rozdziale przyjmujemy 3 warstwy:
1. **Model obliczen** - logika domenowa i obliczenia, bez `print()` i `input()`.
2. **Prezentacja** - formatowanie wyniku dla odbiorcy.
3. **Interakcja** - wejscie/wyjscie, orkiestracja przeplywu, obsluga bledow.
Odnosniki do kodu:
- `examples/layered_grade_app.py`
- `examples/monolith_vs_layers.py`
Diagramy:
- `diagrams/layered_architecture.png`
- `diagrams/request_flow.png`
- `diagrams/testability_map.png`
## 4. Rownowaga teoria/praktyka - wybor 2B
Material celowo laczy oba aspekty:
- teoria: idea Dijkstry, definicja SoC, relacja SoC-SRP,
- praktyka: kod warstwowy, porownanie z monolitem, testy i zadania.
Taki balans jest szczegolnie pomocny dla studentow I roku.
## 5. Monolit vs warstwy
Monolit jest prosty na start, ale z czasem utrudnia testowanie i refaktoryzacje. Podzial warstwowy zmniejsza coupling i poprawia czytelnosc.
Przyklad monolitu i refaktoryzacji znajdziesz w:
- `examples/monolith_vs_layers.py`
## 6. Uruchamianie
```bash
python src/_02-functions/06-separation-of-concerns/examples/monolith_vs_layers.py
python src/_02-functions/06-separation-of-concerns/examples/layered_grade_app.py
python -m pytest src/_02-functions/06-separation-of-concerns/exercises/test_solutions.py -v
```
## 7. Zadania
Pliki:
- `exercises/tasks.py`
- `exercises/solutions_separation_of_concerns.py`
- `exercises/test_solutions.py`
Zakres zadan obejmuje parsowanie, walidacje, obliczenia wazone, decyzje PASS/FAIL, prezentacje i orkiestracje przeplywu.
## 8. Further Considerations (Twoje wybory)
- **1. B**: sekcja Dijkstry ma 2-3 akapity i cytat.
- **2. B**: zachowany balans teoria/praktyka.
- **3**: ponizej gotowy szkic naglowkow i podpunktow dodany jako kolejne tresci.
### 8.1 Szkic 1:1 do dalszej rozbudowy README
1. Kontekst historyczny SoC (Dijkstra)
2. Definicja SoC i granice odpowiedzialnosci
3. SoC vs SRP
4. Architektura warstwowa: model / presentation / interaction
5. Monolit vs warstwy
6. Testowalnosc warstw
7. Uruchomienie przykladow
8. Zadania do samodzielnego wykonania
9. Diagramy i mapowanie na kod
10. Podsumowanie i dalsze kroki
## 9. Referencje
- Dijkstra, E. W., *On the role of scientific thought*.
- Martin, R. C., *Clean Code*.
- Martin, R. C., *Clean Architecture*.
- https://www.cs.utexas.edu/~EWD/
- https://en.wikipedia.org/wiki/Separation_of_concerns
- https://docs.pytest.org/
