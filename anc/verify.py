#!/usr/bin/env python3
"""Exact check of the lattice-point counts in the note (standard library only).

    python3 verify.py [N]        all legs 1 <= a, b <= N (default 30; a few seconds)

For every pair (a, b) it counts by brute force the lattice points of the tilted
square, of the triangle and of the box, and checks Lemmas 1-3, the partition of the
box, the formula for the interior count, Pick's formula and the additive identity
behind it. It also checks that the shear (x, y) -> (x + y, y) changes none of the counts.
"""
import sys
from fractions import Fraction as Fr
from math import gcd


def counts(poly, box):
    """(interior, boundary) lattice points of a convex counterclockwise polygon."""
    edges = list(zip(poly, poly[1:] + poly[:1]))
    interior = boundary = 0
    x0, x1, y0, y1 = box
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            signs = [(q[0] - p[0]) * (y - p[1]) - (q[1] - p[1]) * (x - p[0]) for p, q in edges]
            if all(s > 0 for s in signs):
                interior += 1
            elif all(s >= 0 for s in signs):
                boundary += 1
    return interior, boundary


def area(poly):
    edges = zip(poly, poly[1:] + poly[:1])
    return Fr(sum(p[0] * q[1] - q[0] * p[1] for p, q in edges), 2)


def main(n):
    pairs = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            d, s = gcd(a, b), a + b
            square = [(0, b), (a, 0), (s, a), (b, s)]
            tri = [(0, 0), (a, 0), (0, b)]
            i_sq, b_sq = counts(square, (0, s, 0, s))
            i_tr, b_tr = counts(tri, (0, a, 0, b))
            assert b_sq == 4 * d, "Lemma 2"
            assert b_tr == a + b + d, "Lemma 1"
            assert 2 * i_tr == (a - 1) * (b - 1) - (d - 1), "Lemma 3"
            assert (s - 1) ** 2 == i_sq + 4 * i_tr + 4 * (d - 1), "box partition"
            assert i_sq == a * a + b * b + 1 - 2 * d, "interior count"
            assert area(square) == a * a + b * b == i_sq + Fr(b_sq, 2) - 1, "Pick"
            f_tr = i_tr + Fr(b_tr, 2) - 1
            assert f_tr == Fr(a * b, 2) and s * s - 4 * f_tr == a * a + b * b, "additive identity"
            sheared = [(x + y, y) for x, y in square]
            assert counts(sheared, (0, 2 * s, 0, s)) == (i_sq, b_sq), "shear"
            pairs += 1
    print(f"PASS  Lemmas 1-3, the box partition, the interior count, Pick and the shear, "
          f"for all {pairs} pairs of legs up to {n}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30)
