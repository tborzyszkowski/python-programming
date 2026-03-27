class TemperatureSensor:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius
        self.__calibration_offset = 0.0

    def set_calibration(self, delta: float) -> None:
        self.__calibration_offset = delta

    def read(self) -> float:
        return self._celsius + self.__calibration_offset

    def is_overheated(self, threshold: float) -> bool:
        return self.read() > threshold
