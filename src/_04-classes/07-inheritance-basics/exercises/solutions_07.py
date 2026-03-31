class Vehicle:
    def move(self) -> str:
        return "Pojazd przemieszcza sie"


class Train(Vehicle):
    def move(self) -> str:
        return "Pociąg jedzie po torach"
