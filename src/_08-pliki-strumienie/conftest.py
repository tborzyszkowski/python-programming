"""Konfiguracja testów dla modułu _08-pliki-strumienie.

Przy --import-mode=importlib (ustawione w pytest.ini) pytest
importuje każdy moduł z pełną ścieżką, więc wiele plików
o nazwie 'solutions.py' w różnych katalogach nie koliduje ze sobą.
Ręczne wstrzykiwanie do sys.path nie jest potrzebne.
"""
