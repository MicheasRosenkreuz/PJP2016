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
    # return trickyHull(a, b, c, d)  # pretty simple solution.
    return usingAngle(a, b, c, d)


def usingAngle(*points):
    for i in points:
        vectors = []
        for j in points:  # points different to i
            if i == j: continue
            vectors.append([j[0] - i[0], j[1] - i[1]])
        if len(vectors) != 3 or not IsVectorInsideHull(vectors):
            return False
    return True


def usingArea(*points):
    pass


def IsVectorInsideHull(vectors):
    return 0 < (angle(vectors[0], vectors[1]) + angle(vectors[1], vectors[2]) + angle(vectors[0], vectors[2]))/2 < pi


def angle(v1, v2):
    scalar_sum = v1[0]*v2[0]+v1[1]*v2[1]
    v1_len = sqrt(v1[0]**2+v1[1]**2)
    v2_len = sqrt(v2[0]**2+v2[1]**2)
    return acos(scalar_sum/(v1_len*v2_len))


def trickyHull(*points):
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
