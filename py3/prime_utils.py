#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : prime_utils.py
# Author            : Kaushik S Kalmady
# Date              : 27.11.2017
# Last Modified Date: 10.12.2017
# Last Modified By  : Kaushik S Kalmady

from math import sqrt


def seive(n):
    """Seive of Eratosthenes
    Returns a list of primes less than n
    """
    myseive = [False] * (n)

    for i in range(2, int(sqrt(n)) + 1):
        if not myseive[i]:
            for j in range(i * i, n, i):
                myseive[j] = True

    return [i for i, num in enumerate(myseive) if num is False and i > 1]


def phi(n):
    """Returns the Euler Totient Function of n
    phi(n) = number of positive integers co-prime with n.

    Args:
        n: integer

    REFERENCES
    ==========
    http://www.geeksforgeeks.org/eulers-totient-function/

    EXAMPLES
    ========
    >>> phi(10)
    4
    >>> phi(7)
    6
    >>> phi(33500000)
    13200000
    """
    result = n
    p = 2
    while p * p <= n:
        if not n % p:
            while not n % p:
                n /= p
            result -= result / p
        p += 1
    if n > 1:  # Occurs when prime factor p > sqrt(n), there is one such number
        result -= result / n
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
