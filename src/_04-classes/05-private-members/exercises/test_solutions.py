from solutions_05 import TemperatureSensor


def test_is_overheated() -> None:
    sensor = TemperatureSensor(70.0)
    sensor.set_calibration(5.0)
    assert sensor.is_overheated(72.0)
