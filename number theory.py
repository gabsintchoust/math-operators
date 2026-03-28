from math import log2, sqrt

def square(a, b):
    x = b / 2
    return a ** x

def prime(n):
    limit = int(sqrt(n))
    sieve = list(range(n + 1))
    i = 2
    while i <= limit:
        if sieve[i] != 0:
            j = i + i
            while j <= n:
                sieve[j] = 0
                j += i
        i += 1
    primes = [p for p in sieve if p != 0 and p != 1]
    return primes

def hexagon(n):
    return ((2 * n) - 1) * n

def hextoperfect(n):
    return hexagon(2 ** (n - 1))

def perftoprime(n):
    if n % 2 != 0:
        return None
    s = n + 1
    t = n // 2
    if (t & (t - 1)) != 0:
        return None
    p = int(log2(t)) + 1
    mersenne = (2 ** p) - 1
    if n == (2 ** (p - 1)) * mersenne:
        return p
    else:
        return None

def primetoprime(n):
    if n is None:
        return None
    nn = [n]
    while log2(nn[-1] + 1) == int(log2(nn[-1] + 1)):
        nn.append(int(log2(nn[-1] + 1)))
    return nn

def number(n):
    a = n
    b = a - 1
    c = hextoperfect(a)
    d = perftoprime(c)
    if d is not None:
        return a, b, c, d, primetoprime(d)
    else:
        return None