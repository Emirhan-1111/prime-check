# prime-check

[![tests](https://github.com/Emirhan-1111/prime-check/actions/workflows/tests.yml/badge.svg)](https://github.com/Emirhan-1111/prime-check/actions/workflows/tests.yml)

Determine whether a number is prime — and if it is not, show its prime factorization.

```
$ python prime_check.py 97 91 1 2147483647
97 is prime
91 is not prime: 91 = 7 × 13
1 is not prime: primes start at 2
2147483647 is prime
```

## How it works

`is_prime` uses trial division with the two shortcuts that make it fast enough for
everyday numbers:

- even numbers other than 2 are rejected at once,
- only odd divisors up to **√n** are tried — if `n = a · b` with `a ≤ b`, then `a ≤ √n`,
  so a divisor above √n would have a partner below it that was already found.

That is about √n / 2 divisions in the worst case: instant for numbers up to around 10¹⁴.
`factorize` divides out each factor as soon as it is found, so `600851475143` splits into
`71 × 839 × 1471 × 6857` in a fraction of a millisecond.

## Use

```bash
python prime_check.py            # asks for a number
python prime_check.py 97 91      # or several at once
```

```python
from prime_check import is_prime, factorize
is_prime(97)        # True
factorize(360)      # [2, 2, 2, 3, 3, 5]
```

The tests compare `is_prime` with a sieve of Eratosthenes for every number up to 20 000.

## License

MIT, see [LICENSE](LICENSE).
