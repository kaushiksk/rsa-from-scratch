#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : utils.py
# Author            : Kaushik S Kalmady
# Date              : 24.11.2017
# Last Modified Date: 24.11.2017
# Last Modified By  : Kaushik S Kalmady


def exp(x, n, p):
    """exp
    returns x^n mod p

    :param x: base
    :param n: power
    :param p: mod value
    """
    ans = x

    while n > 1:
        ans = (ans * ans) % p
        if n % 2:
            ans = (ans * x) % p
        n = n >> 1

    return ans


if __name__ == "__main__":
    print(exp(2, 47, 1000007))
