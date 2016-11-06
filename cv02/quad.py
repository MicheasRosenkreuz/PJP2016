#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP 2016 - cvičení číslo 2
"""
from math import acos, sqrt, pi


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
    # return tricky_hull(a, b, c, d)  # pretty simple solution.
    # return using_area(a, b, c, d)
    return using_angle(a, b, c, d)


def using_angle(*points):
    """
    Zjednodušeně: tato metoda testuje zda se bod nachází vně convexhull(v tomto případě trojuhelník).
    součet úhlu mezi vektory tvořeným testovaným bodem a těmy ostatními nesmí být větší jak půlkruh.
    """
    for i in points:
        vectors = []
        for j in points:  # points different to i
            if i == j:
                continue
            vectors.append([j[0] - i[0], j[1] - i[1]])
        if len(vectors) != 3 or not _is_vector_inside_hull(vectors):
            return False
    return True


def using_area(*points):
    """
    Tato metoda počítá obsach všech trojúhelníků, které body mohou tvořit.
    Jestliže součet obsahu tří nejmenších trojúhelníku je roven obsahu největšího, pak se jedná
    o konkávní čtyřúhelník.
    """
    area = []
    for p in points:
        t = list(filter(lambda x: x != p, points))
        if len(t) != 3:
            return False
        edges = [[t[0][0] - t[1][0], t[0][1] - t[1][1]],
                 [t[1][0] - t[2][0], t[1][1] - t[2][1]],
                 [t[0][0] - t[2][0], t[0][1] - t[2][1]]]
        edg = list(map(lambda x: sqrt(x[0] ** 2 + x[1] ** 2), edges))
        # Heronův vzorec
        s = sum(edg) / 2
        area.append(round(sqrt(s * (s - edg[0]) * (s - edg[1]) * (s - edg[2])), 10))
    area.sort()
    # Pokud součet 3 nejmenčích ploch je roven největší ploše, pak se jedná o konkávní čtyřúhelník
    return sum(area[:3]) != area[3]


def _is_vector_inside_hull(vectors):
    return 0 < \
           (_angle(vectors[0], vectors[1]) + _angle(vectors[1], vectors[2]) + _angle(vectors[0], vectors[2])) / 2\
           < pi


def _angle(v1, v2):
    scalar_sum = v1[0] * v2[0] + v1[1] * v2[1]
    v1_len = sqrt(v1[0] ** 2 + v1[1] ** 2)
    v2_len = sqrt(v2[0] ** 2 + v2[1] ** 2)
    return acos(scalar_sum / (v1_len * v2_len))


def tricky_hull(*points):
    """
    This solution uses library from scipy to construct convex hull
    If convex hull have'nt 4 vertices then it is not convex quadrilateral
    """
    from scipy.spatial import ConvexHull
    from scipy.spatial.qhull import QhullError
    try:
        hull = ConvexHull(points)
    except QhullError:
        return False
    return len(hull.vertices) == 4


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
