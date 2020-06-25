import random

def RabinMiller(n, d):
    a = 2 + random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)# a^d%n
    if x == 1 or x == n-1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False

def isPrime(n):
    """
    return True if n is prime
    """

    # (-inf, 1) numbers not prime
    if n < 2:
        return False

    # low prime numbers to save time
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    # if in lowPrimes
    if n in lowPrimes:
        return True
    
    # if low primes divide into n
    for prime in lowPrimes:
        if n % prime == 0:
            return False
    
    # Find number ch such that c * 2 ^ r = n -1
    ch = n - 1 # ch even be n no divisible by 2
    while ch % 2 == 0:
        ch /= 2 # make ch odd

    # prove not prime 128 times
    for _ in range(128):
        if not RabinMiller(n, ch):
            return False

    return True


def keygen(keysize = 1024):
    e = d = N = 0

    # get primes p and q
    p = Primegen(keysize)
    q = Primegen(keysize)

    N = p * q # RSA Modulus
    phiN = (p - 1) * (q - 1) # Phi function

    # Choose e, which is coprime with phiN and 1 < e <= phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoprime(e, phiN)):
            break
    
    d = modularInv(e, phiN)

    return e, d, N

def Primegen(keysize):
    """
    Returns random large prime number
    """

    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num

def isCoprime(p, q):
    """
    return True if gcd(p, q) is 1 
    """

    return gcd(p, q) == 1

def gcd(p, q):
    """
    Euclidean Algorithm to find gcd of p and q
    """

    while q:
        p, q = q, p % q
    
    return p

def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_r, old_s, old_t

def modularInv(a, b):
    _, x,_ = egcd(a, b)

    if x < 0:
        x += b

    return x                 

def encrypt(e, N, m):
    c = ""

    for ch in m:
        z = ord(ch)
        c += str(pow(z, e, N)) + " "

    return c

def decrypt(d, N, c):
    m = ""

    parts = c.split()
    for part in parts:
        if part:
            ch = int(part)
            m += chr(pow(ch, d, N))

    return m

def main():
    
    keysize = 128

    e, d, N = keygen(keysize)

    m = "Hello World"
    
    enc = encrypt(e, N, m)
    dec = decrypt(d, N, enc)

    print(f"Message: {m}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")

main()