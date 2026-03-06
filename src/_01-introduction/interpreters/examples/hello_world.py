"""
Demonstracja: jak Python kompiluje kod do bajtkodu i jak go obejrzeć.
Uruchomienie: python hello_world.py
"""
import dis
import sys


def greet(name: str) -> str:
    """Prosta funkcja powitalna."""
    return f"Witaj, {name}!"


def add(a: float, b: float) -> float:
    """Dodawanie dwóch liczb."""
    return a + b


if __name__ == "__main__":
    # Podstawowe uruchomienie
    print(greet("Python"))
    print(f"2 + 3 = {add(2, 3)}")

    print("\n" + "=" * 50)
    print(f"Wersja Pythona: {sys.version}")
    print(f"Implementacja:  {sys.implementation.name}")

    # Podgląd bajtkodu funkcji greet()
    print("\n--- Bajtkod funkcji greet() ---")
    dis.dis(greet)

    # Podgląd bajtkodu funkcji add()
    print("\n--- Bajtkod funkcji add() ---")
    dis.dis(add)

    # Informacja o pliku .pyc
    import importlib.util
    spec = importlib.util.find_spec("dis")
    print(f"\nModuł 'dis' pochodzi z: {spec.origin}")

