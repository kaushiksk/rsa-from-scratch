#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : gcd_utils.py
# Author            : Kaushik S Kalmady
# Date              : 27.11.2017
# Last Modified Date: 01.12.2017
# Last Modified By  : Kaushik S Kalmady


def gcd(a, b):
    """Euclid's algorithm for gcd

    Args:
        a: int
        b: int

   Returns gcd(a, b) computed using Euclid's Algorithm.

    >>> gcd(7, 19)
    1
    >>> gcd(221,34)
    17
    """
    if a == 0:
        return b

    return gcd(b % a, a)


def xgcd(a, b):
    """Extended Euclidean Algorithm

    Args:
        a: int
        b: int

    We can represent gcd(a,b) = a.x + b.y
    This function returns gcd(a, b), x, y

    Why does it work?
    a.x + b.y = (b % a).x1 + a.y1
            = (b - (b//a).a).x1 + a.y1
            = a.(y1 - (b//a).x1) + b.x1

    >>> xgcd(15, 35)
    (5, -2, 1)
    >>> xgcd(30, 20)
    (10, 1, -1)
    """
    if a == 0:
        return (b, 0, 1)

    g, x, y = xgcd(b % a, a)

    return (g, y - (b//a) * x, x)


def inverse(a, n):
    """Modular Multiplicative Inverse

    Args:
        a: integer whose inverse is to be found
        n: modular base

    Returns the modular multiplicative inverse of 'a' under mod n
    Return value is always positive

    >>> inverse(2, 5)
    3
    >>> inverse(17, 39)
    23
    >>> inverse(2,4)
    Traceback (most recent call last):
    Exception: Inverse does not exist.

    """
    g, x, _ = xgcd(a, n)

    if g != 1:
        raise Exception("Inverse does not exist.")

    return (x % n + n) % n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
