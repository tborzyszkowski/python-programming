"""Dziedziczenie w Pythonie – hierarchia pojazdów."""
from __future__ import annotations


class Vehicle:
    """Klasa bazowa dla wszystkich pojazdów."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self._make = make
        self._model = model
        self._year = year
        self._speed: float = 0.0

    def __str__(self) -> str:
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._make!r}, {self._model!r}, {self._year})"

    def move(self) -> str:
        return "Pojazd przemieszcza się"

    def stop(self) -> None:
        self._speed = 0.0

    def accelerate(self, delta: float) -> None:
        self._speed = max(0.0, self._speed + delta)

    def info(self) -> str:
        return f"{self} | prędkość: {self._speed:.1f} km/h"


class Bike(Vehicle):
    """Rower – bez silnika, ze skrzynią biegów."""

    def __init__(self, make: str, model: str, year: int, gears: int = 21) -> None:
        super().__init__(make, model, year)   # wywołanie konstruktora klasy bazowej
        self._gear = 1
        self._gears = gears

    def move(self) -> str:
        return f"Rower jedzie (bieg {self._gear}/{self._gears})"

    def shift_gear(self, up: bool = True) -> None:
        if up and self._gear < self._gears:
            self._gear += 1
        elif not up and self._gear > 1:
            self._gear -= 1


class Car(Vehicle):
    """Samochód spalinowy."""

    def __init__(self, make: str, model: str, year: int, fuel: float = 50.0) -> None:
        super().__init__(make, model, year)
        self._fuel = fuel
        self._fuel_capacity = 60.0

    def move(self) -> str:
        if self._fuel <= 0:
            return "Brak paliwa!"
        self._fuel -= 0.1 * self._speed / 10
        return f"Samochód jedzie (paliwo: {self._fuel:.1f} L)"

    def refuel(self, liters: float) -> None:
        self._fuel = min(self._fuel_capacity, self._fuel + liters)

    def fuel_level(self) -> float:
        return self._fuel


class ElectricCar(Car):
    """Samochód elektryczny – rozszerzenie Car."""

    def __init__(self, make: str, model: str, year: int, battery: float = 100.0) -> None:
        super().__init__(make, model, year, fuel=0.0)  # brak paliwa
        self._battery = battery

    def move(self) -> str:
        if self._battery <= 0:
            return "Brak energii!"
        self._battery -= 0.5
        return f"Samochód elektryczny jedzie (bateria: {self._battery:.1f}%)"

    def charge(self, kwh: float) -> None:
        self._battery = min(100.0, self._battery + kwh)

    def battery_level(self) -> float:
        return self._battery


def main() -> None:
    vehicles: list[Vehicle] = [
        Bike("Trek", "FX3", 2023),
        Car("Toyota", "Corolla", 2022, fuel=40.0),
        ElectricCar("Tesla", "Model 3", 2024, battery=80.0),
    ]

    for v in vehicles:
        v.accelerate(60)
        print(v.move())    # ← polimorfizm
        print(v.info())
        print()

    # Pokazanie MRO
    print("MRO ElectricCar:")
    for cls in ElectricCar.__mro__:
        print(f"  {cls.__name__}")


if __name__ == "__main__":
    main()
