#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP 2016 - cvičení číslo 2
"""
from scipy.spatial import Delaunay


def in_hull(p, hull):
    """
    Test if points in `p` are in `hull`

    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the
    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
    will be computed
    """
    if not isinstance(hull, Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p) >= 0


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí,
    zda tvoří konvexní čtyřúhelník.

    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří.
    """
    return a == b == c == d


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
