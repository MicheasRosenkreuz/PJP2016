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
import sys

import doors
import importlib
runpy = importlib.import_module('__main__', doors)


def test_1_max_true():
    """
    doors: 1
    locks: max
    expect: True
    """
    filename = 'doors.txt'
    assert list(doors.doors(filename)) == [True, ]


def test_3_100_true():
    """
    doors: 3
    locks: 3x100
    expect: all True
    """
    filename = 'doors1.txt'
    assert list(doors.doors(filename)) == [True, True, True]


def test_1_max_false():
    """
    doors: 1
    locks: max
    expect: False
    """
    filename = 'false_doors.txt'
    assert list(doors.doors(filename)) == [False, ]


def test_small():
    """
    doors: 1
    locks: max
    expect: False
    """
    filename = 'small.txt'
    assert list(doors.doors(filename)) == [False, True, False]


def test_small_alt():
    """
    mnohem pomalejsi algoritmus ~O(n^M)
    """
    filename = 'small.txt'
    assert list(doors.doors(filename, doors._alternative)) == \
           [False, True, False]


def test_large():
    """
    doors: 1
    locks: max
    expect: False
    """
    filename = 'large.txt'
    assert list(doors.doors(filename)) == [False, False]
