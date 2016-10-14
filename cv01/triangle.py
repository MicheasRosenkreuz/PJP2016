# -*- coding: utf8 -*-
import math


def triangle(a, b, c):
    """
    Funkce vraci True nebo False, podle toho zda strany a, b, c mohou tvorit
    pravouhly trojuhelnik
    """
    a, b, c = sorted([a, b, c])
    return c == math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    assert triangle(3, 4, 5)
