import numpy
import rsa
import sympy
import random

big_primes = [
        5915587277,
        1500450271,
        3267000013,
        5754853343,
        4093082899
]
small_primes = [
    16447,
    16487,
    16529,
    16561,
    16619 
]
prime_pool_1 = [
    71755440315342536873,
    45095080578985454453,
    27542476619900900873,
    66405897020462343733,
    36413321723440003717,
    4384165182867240584805930970951575013697,
    5991810554633396517767024967580894321153,
    6847944682037444681162770672798288913849,
    4146162919458530168953357282201621124057,
    5570373270183181665098052481109678989411,
    64495327731887693539738558691066839103388567300449,
    58645563317564309847334478714939069495243200674793,
    48705091355238882778842909230056712140813460157899,
    15452417011775787851951047309563159388840946309807,
    53542885039615245271174355315623704334284773568199
]
prime_pool_2 = [
    48112959837082048697,
    54673257461630679457,
    29497513910652490397,
    40206835204840513073,
    12764787846358441471,
    2425967623052370772757633156976982469681,
    1451730470513778492236629598992166035067,
    6075380529345458860144577398704761614649,
    3615415881585117908550243505309785526231,
    5992830235524142758386850633773258681119,
    22953686867719691230002707821868552601124472329079,
    30762542250301270692051460539586166927291732754961,
    29927402397991286489627837734179186385188296382227,
    46484729803540183101830167875623788794533441216779,
    95647806479275528135733781266203904794419563064407,
]

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, int(n/i))

def carmichael(p, q):
    gcd, _, _ = egcd(p-1, q-1)
    return int((p-1)*(q-1) / gcd)

def mod_exp(base, exponent, mod):
    binary_rep = "{0:b}".format(exponent)

    squares = [base]
    for _ in binary_rep[:-1]:
        squares.insert(0, squares[0]**2 % mod)

    res = 1
    for i, bit in enumerate(binary_rep):
        if bit == '1':
            res = res * squares[i] % mod
    return res

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x) 

def modular_inverse(e, mod):
    _, d, _ = egcd(e, mod)
    return d if d>0 else d+mod

def decipher(d, n, c):
    return mod_exp(c,d,n)

def encipher(e, n, m):
    return m ** e % n

def bruteforce(m):
    for p, q in zip(small_primes, big_primes):
        e = 65537
        n = p*q
        c = encipher(e, n, m)
        print("cipher =", c)
        factors = factorize(n)
        phi_n = carmichael(factors[0], factors[1])
        d = modular_inverse(e, phi_n) 
        print("found exponent d =", d)
        plain = decipher(d, n, c)
        print("deciphered =",plain)
    	
def main():
    keys_public = [
        random.choice(prime_pool_1)*random.choice(prime_pool_2)
        for _ in range(10)
    ]

    # BRUTEFORCE TEST
    # m = int(input("input m: "))
    # bruteforce(m)

    # GCD TEST
    # for i in keys_public:
    #     for j in keys_public:
    #         if i == j:
    #             continue
    #         print("GCD:",egcd(i,j)[0])

if __name__ == "__main__":
    main()