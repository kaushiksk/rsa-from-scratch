#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : gcd_utils.py
# Author            : Kaushik S Kalmady
# Date              : 27.11.2017
# Last Modified Date: 11.12.2017
# Last Modified By  : Kaushik S Kalmady


def recursive_gcd(a, b):
    """Euclid's algorithm for gcd (Recursive)

    Args:
        a: int
        b: int

    Returns gcd(a, b) computed using Euclid's Algorithm.

    EXAMPLES
    ========
    >>> gcd(7, 19)
    1
    >>> gcd(221,34)
    17
    """
    if a == 0:
        return b

    return recursive_gcd(b % a, a)


def gcd(a, b):
    """Euclid's algorithm for gcd (Iterative)

    Args:
        a: int
        b: int

    Returns gcd(a, b) computed using Euclid's Algorithm.

    EXAMPLES
    ========
    >>> gcd(7, 19)
    1
    >>> gcd(221,34)
    17
    """
    assert a > 0 and b > 0

    while a:
        a, b = b % a, a

    return b


def recursive_xgcd(a, b):
    """Extended Euclidean Algorithm (Recursive)

    Args:
        a: int
        b: int

    NOTES
    =====
    We can represent gcd(a,b) = a.x + b.y
    This function returns gcd(a, b), x, y

    Why does it work?
    a.x + b.y = (b % a).x1 + a.y1
              = (b - (b//a).a).x1 + a.y1
              = a.(y1 - (b//a).x1) + b.x1

    REFERENCES
    ==========
    http://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

    EXAMPLES
    ========
    >>> xgcd(15, 35)
    (5, -2, 1)
    >>> xgcd(30, 20)
    (10, 1, -1)
    """
    if a == 0:
        return (b, 0, 1)

    g, x, y = xgcd(b % a, a)

    return (g, y - (b//a) * x, x)


def xgcd(a, b):
    """Extended Euclidean Algorithm (Iterative)

    Args:
        a: int
        b: int

    NOTES
    =====
    We can represent gcd(a,b) = a.x + b.y
    This function returns gcd(a, b), x, y

    REFERENCES
    ==========
    https://anh.cs.luc.edu/331/notes/xgcd.pdf

    EXAMPLES
    ========
    >>> xgcd(15, 35)
    (5, -2, 1)
    >>> xgcd(30, 20)
    (10, 1, -1)
    """
    assert a > 0 and b > 0

    xprev, x = 1, 0
    yprev, y = 0, 1

    while a:
        q = b // a
        x, xprev = xprev - q * x, x
        y, yprev = yprev - q * y, y
        a, b = b % a, a

    return b, xprev, yprev


def inverse(a, n):
    """Modular Multiplicative Inverse

    Args:
        a: integer whose inverse is to be found
        n: modular base

    NOTES
    =====
    Returns the modular multiplicative inverse of 'a' under mod n
    Return value is always positive

    EXAMPLES
    ========
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
