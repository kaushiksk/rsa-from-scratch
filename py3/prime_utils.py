#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : prime_utils.py
# Author            : Kaushik S Kalmady
# Date              : 27.11.2017
# Last Modified Date: 27.11.2017
# Last Modified By  : Kaushik S Kalmady

from math import sqrt

from utils import exp


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


def modified_seive(n):
    """Modified Seive of Eratosthenes for calculating Euler's Totient Function

    Returns a list of length n + 1.
    seive[i] is the largest prime that divides i.

    """
    myseive = [0] * (n + 1)
    myseive[0] = myseive[1] = 1

    for i in range(2, n + 1):
        if not myseive[i]:
            myseive[i] = i
            for j in range(i, n + 1, i):
                myseive[j] = i

    return myseive


def phi(n):
    """Returns the Euler Totient Function of n

    phi(n) = number of positive integers co-prime with n.

    """
    ans = 1
    prime = modified_seive(n)

    while(n > 1):
        p = prime[n]
        e = 0
        while(n % p == 0):
            n = n//p
            e += 1
        ans *= (p - 1) * exp(p, e - 1)

    return ans


if __name__ == "__main__":
    import doctest
    doctest.testmod()
