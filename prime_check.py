"""Determine whether a number is prime - and if not, why not.

    $ python prime_check.py 97 91 1
    97 is prime
    91 is not prime: 91 = 7 × 13
    1 is not prime: primes start at 2
"""
import sys


def is_prime(num):
    """Determine whether a given number is prime.

    Parameters:
        num (int): The number to be tested for primality.

    Returns:
        bool: True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def factorize(num):
    """Prime factors of num >= 2 in ascending order, e.g. 360 -> [2, 2, 2, 3, 3, 5]."""
    if num < 2:
        raise ValueError("factorize needs a number of at least 2")
    factors, d = [], 2
    while d * d <= num:
        while num % d == 0:
            factors.append(d)
            num //= d
        d += 1 if d == 2 else 2
    if num > 1:
        factors.append(num)
    return factors


def explain(num):
    """One line telling whether num is prime and, if not, its factorization."""
    if num < 2:
        return f"{num} is not prime: primes start at 2"
    if is_prime(num):
        return f"{num} is prime"
    return f"{num} is not prime: {num} = {' × '.join(map(str, factorize(num)))}"


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if hasattr(sys.stdout, "reconfigure"):          # "×" also when output is redirected on Windows
        sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        argv = [input("Enter an integer: ")]
    for arg in argv:
        try:
            print(explain(int(arg)))
        except ValueError:
            print(f"{arg!r} is not an integer")


if __name__ == "__main__":
    main()
