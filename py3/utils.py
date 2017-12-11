#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : utils.py
# Author            : Kaushik S Kalmady
# Date              : 24.11.2017
# Last Modified Date: 11.12.2017
# Last Modified By  : Kaushik S Kalmady


def exp(x, n, p=1000007):
    """returns x^n mod p

    EXAMPLES
    ========
    >>> exp(2,47)
    199807
    >>> exp(3,51,678)
    93
    """

    ans = 1
    x = x % p

    while n > 0:
        if n & 1:
            ans = (ans * x) % p
        x = (x * x) % p
        n = n >> 1

    return ans


def legendre(a, b):
    """"Calculates the Legendre symbol for the given parameters


    :param a:
    :param b:
    """

    # Since it is internally used we assume the user passes prime b
    # TODO test primality of b here
    return jacobi(a, b)


def jacobi(a, b):
    """Calculates the Jacobi symbol for the given parameters
    If b is prime, it returns the Legendre Symbol.

    REFERENCES
    ==========
    http://2000clicks.com/MathHelp/NumberTh27JacobiSymbolAlgorithm.aspx
    http://primes.utm.edu/glossary/xpage/JacobiSymbol.html

    EXAMPLES
    ========
    >>> jacobi(1001, 9907)
    -1
    >>> jacobi(19, 45)
    1
    >>> jacobi(8,21)
    -1
    >>> jacobi(3, 15)
    0
    >>> jacobi(13, 28)
    Traceback (most recent call last):
    ValueError: b has to be odd
    >>> jacobi(28, 13)
    -1
    """

    if b <= 0:
        raise ValueError("b has to be >= 1")
    if not b & 1:
        raise ValueError("b has to be odd")

    ans = 1
    if a < 0:
        a = -a
        if b % 4 == 3:
            ans = -ans

    while a != 0:
        while not a % 2:
            a /= 2
            if b % 8 in (3, 5):
                ans = -ans
        a, b = b, a
        if a % 4 == 3 and b % 4 == 3:
            ans = -ans
        a = a % b

    if b == 1:
        return ans
    else:
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
