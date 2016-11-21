# -*- coding: utf-8 -*-
"""
@author: Jiri Vrany
@author: Frantisek Jukl
@author: Michal Jirasek

Pro použití je potřeba balíček py.test.
Instaluje se přes pip příkazem pip install pytest.

Zbytek je snadný, nakopírujte tento soubor do adresáře s
řešením a z příkazové řádky
spusťe test - příkazem py.test

Pytest prohledá aktuální adresář (a adresáře vnořené) a spustí
nalezené testy.
"""
import doors


def test_1_max_true():
    """
    doors: 1
    locks: max
    expect: True
    """
    filename = 'doors1.txt'
    assert list(doors.doors(filename)) == [True, ]


def test_3_100_true():
    """
    doors: 3
    locks: 3x100
    expect: all True
    """
    filename = 'f1.txt'
    assert list(doors.doors(filename)) == [True, True, True]
