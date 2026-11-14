from math import prod

import pytest

from prime_check import explain, factorize, is_prime


def test_first_primes():
    assert [n for n in range(50) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                                     37, 41, 43, 47]


def test_against_sieve():
    N = 20000
    sieve = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [False] * len(sieve[i * i::i])
    assert [is_prime(n) for n in range(N + 1)] == sieve


@pytest.mark.parametrize("n,f", [(2, [2]), (91, [7, 13]), (360, [2, 2, 2, 3, 3, 5]),
                                 (2**31 - 1, [2**31 - 1]), (600851475143, [71, 839, 1471, 6857])])
def test_factorize(n, f):
    assert factorize(n) == f and prod(f) == n


def test_explain():
    assert explain(97) == "97 is prime"
    assert explain(91) == "91 is not prime: 91 = 7 × 13"
    assert explain(1) == "1 is not prime: primes start at 2"
    assert explain(-7).startswith("-7 is not prime")
