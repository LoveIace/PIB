
import math
import util
from encryption import encrypt
from decryption import decrypt

def find_possible(public, b1, b2):
    a1 = public[0]
    a2 = public[1]
    factor = a1*b2 - a2*b1
    M_min = max(public)
    M_max = max(public) * 2
    min_factor = math.ceil(M_min / factor)
    max_factor = math.floor(M_max / factor)

    for f in range(min_factor, max_factor + 1):
        M_pos = factor*f
        W_pos = util.find_modular_inverse(b1, M_pos)*a1 % M_pos
        print("possible M:", M_pos, "relative W:",W_pos)
        yield M_pos, W_pos

def main():
    private = [2, 7, 11, 21, 42, 89, 180, 354]
    M = 881
    W = 588
    public = [
        b*W%M for b in private
    ]
    p = [1,0,0,1,0,0,1,1]
    c = encrypt(p, public)
    p = decrypt(c, public, private, M, W)

    possible_solutions = [
        [util.find_modular_inverse(W_pos, M_pos)*a % M_pos for a in public]
        for M_pos, W_pos in find_possible(public, 2, 7)
    ]
    print(possible_solutions)

if __name__ == "__main__":
    main()


