"""
Testy jednostkowe dla modułu running-python.
Uruchomienie: pytest tests/ -v
"""
import sys


class TestRunAsModule:
    """Testy funkcji z pakietu run_as_module."""

    def test_import_pakietu(self):
        from run_as_module import powitaj, oblicz_bmi
        assert callable(powitaj)
        assert callable(oblicz_bmi)

    def test_powitaj(self):
        from run_as_module import powitaj
        wynik = powitaj("Test")
        assert "Test" in wynik

    def test_bmi_prawidlowy(self):
        from run_as_module import oblicz_bmi
        bmi = oblicz_bmi(70, 1.75)
        assert bmi == round(70 / 1.75 ** 2, 2)

    def test_bmi_zakres(self):
        from run_as_module import oblicz_bmi
        # Normalna waga: BMI 18.5–24.9
        bmi = oblicz_bmi(70, 1.75)
        assert 18.0 < bmi < 25.0

    def test_bmi_zero_wzrost(self):
        from run_as_module import oblicz_bmi
        try:
            oblicz_bmi(70, 0)
            assert False, "Powinien rzucić ValueError"
        except ValueError:
            pass

    def test_bmi_ujemny_wzrost(self):
        from run_as_module import oblicz_bmi
        try:
            oblicz_bmi(70, -1.0)
            assert False, "Powinien rzucić ValueError"
        except ValueError:
            pass


class TestDunderName:
    """
    Testy sprawdzające zachowanie __name__ w skryptach i modułach.
    """

    def test_modul_ma_nazwe_nie_main(self):
        """Importowany moduł ma __name__ != '__main__'."""
        import run_as_module.main as m  # type: ignore[import]
        assert m.__name__ != "__main__"

    def test_pakiet_ma_wersje(self):
        """Pakiet powinien eksponować __version__."""
        import run_as_module as pkg  # type: ignore[import]
        assert hasattr(pkg, "__version__")
        assert pkg.__version__ == "1.0.0"


class TestSysArgv:
    """
    Testy sprawdzające obsługę sys.argv w skrypcie.
    sys.argv[0] to zawsze nazwa skryptu / pytest podczas testów.
    """

    def test_sys_argv_jest_lista(self):
        assert isinstance(sys.argv, list)

    def test_sys_argv_nie_pusty(self):
        assert len(sys.argv) >= 1



