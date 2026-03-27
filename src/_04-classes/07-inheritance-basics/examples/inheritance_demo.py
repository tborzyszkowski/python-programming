class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza się"


class Bike(Vehicle):
    def move(self) -> str:
        return "Rower jedzie"


class Car(Vehicle):
    def move(self) -> str:
        return "Samochód jedzie"
