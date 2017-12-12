#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : primality_tests.py
# Author            : Kaushik S Kalmady
# Date              : 11.12.2017
# Last Modified Date: 12.12.2017
# Last Modified By  : Kaushik S Kalmady

import random

from utils import exp, jacobi


def fermats_test(n, k=10):
    """Fermat's Primality test
    Returns True(probably prime) if n is prime, Flase if n is composite.

    Args:
        n: integer to be tested for primality
        k: number of iterations of the Fermat's Primality Test

    NOTES
    =====
    Not very efficient for large integers as exp is costly
    Carmichael numbers can bypass this test
    https://en.wikipedia.org/wiki/Fermat_primality_test#Flaw

    REFERENCES
    ==========
    https://en.wikipedia.org/wiki/Primality_test#Fermat_primality_test

    EXAMPLES
    ========
    >>> fermats_test(5)
    True
    >>> fermats_test(4)
    False
    >>> fermats_test(341)
    False

    The test may fail for n = 561 = 3.11.17, the smallest Carmichael number if
    we add the condition that the chosen 'a' values have to be co-prime to n.
    >>> fermats_test(561)
    False
    """
    if n == 2:
        return True
    if not n % 2:
        return False

    # Check if a^(n-1) = 1 mod n for k different a values
    for _ in range(k):
        a = random.randint(2, n-1)
        if exp(a, n - 1, n) != 1:
            return False
    return True


def miller_rabin(n, k=10):
    """Miller Rabin Primality Test
    Return False if n is composite, True(probably prime) otherwise.

    Args:
        n: integer to be tested for primality
        k: number of iterations to run the test

    NOTES
    =====
    If n is composite then the Miller–Rabin primality test declares n probably
    prime with a probability at most 4^(−k). Hence, larger the value of k we
    choose, better is the chance of reducing false positives.

    REFERENCES
    ==========
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    EXAMPLES
    ========
    >>> miller_rabin(561)
    False
    >>> miller_rabin(29)
    True
    >>> miller_rabin(221)
    False
    """
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    # Represent n - 1 as (2^s)*d
    s, d = 0, n - 1
    while not d % 2:
        s += 1
        d //= 2
    assert(2**s*d == n - 1)

    def check_if_composite_using(a):
        x = exp(a, d, n)
        if x == 1 or x == n - 1:
            return False  # probably prime
        for _ in range(s):
            x = (x * x) % n  # check for each a^((2^i)*d)
            if x == n - 1:
                return False  # probably prime
        return True  # definitely composite

    # Test for k random integers a
    for _ in range(k):
        a = random.randint(2, n-1)
        if check_if_composite_using(a):
            return False  # definitely composite
    return True  # probably prime


def solovay_strassen(n, k=10):
    """Solovay Strassen Primality Test
    Returns False is n is composite, True(probably prime) otherwise.

    Args:
        n: integer to be tested for primality
        k: number of iterations to run the test

    NOTES
    =====
    It is possible for the algorithm to return an incorrect answer.
    If the input n is indeed prime, then the output will always correctly be
    probably prime. However, if the input n is composite then it is possible
    for the output to be incorrectly probably prime.
    The number n is then called a Euler-Jacobi pseudoprime.

    The probability of failure is at most 2^(-k)

    REFERENCES
    ==========
    https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test

    EXAMPLES
    >>> solovay_strassen(561)
    False
    >>> solovay_strassen(29)
    True
    >>> solovay_strassen(221)
    False
    """

    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = (jacobi(a, n) + n) % n  # map -1 to n - 1
        if x == 0 or exp(a, (n - 1)//2, n) != x:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
