#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : utils.py
# Author            : Kaushik S Kalmady
# Date              : 24.11.2017
# Last Modified Date: 24.11.2017
# Last Modified By  : Kaushik S Kalmady


def exp(x, n, p):
    """returns x^n mod p

    >>> exp(2,47,1000007)
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
