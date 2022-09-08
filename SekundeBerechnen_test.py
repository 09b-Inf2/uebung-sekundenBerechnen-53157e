import SekundenBerechnen
import builtins

def test_SekundeBerechnen(monkeypatch):
    inputs = iter(['7', '21', '37'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = SekundenBerechnen.sekundenBerechnen()
    print(result)
    assert result == '7 Stunden, 21 Minuten und 37 Sekunden sind insgesamt 26497 Sekunden.'
