#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : prime_utils.py
# Author            : Kaushik S Kalmady
# Date              : 27.11.2017
# Last Modified Date: 27.11.2017
# Last Modified By  : Kaushik S Kalmady


def seive(n):
    """Seive of Eratosthenes

    Returns a list of primes less than n
    """
    pass

def modified_seive(n):
    """Modified Seive of Eratosthenes for calculating Euler's Totient Function

    Returns a list of length n.
    seive[i] is the largest prime that divides i.

    """
    pass


def phi(n):
    """Returns the Euler Totient Function of n

    phi(n) = number of positive integers co-prime with n.

    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
