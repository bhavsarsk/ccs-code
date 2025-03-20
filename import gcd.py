import math
                           # name shantanu bhavsar 
                            # roll no 15
                            # prn uit22m1017
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def mod_inverse(e, phi):

    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("e is not invertible")
    if t < 0:
        t = t + phi
    return t

def main():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1

    d = mod_inverse(e, phi)
    print("\nPublic Key: ({e}, {n})")
    print("Private Key: ({d}, {n})")

    message = int(input("\nEnter a number to encrypt (should be < {n}): "))

    encrypted = mod_exp(message, e, n)
    print("Encrypted message: {encrypted}")

    decrypted = mod_exp(encrypted, d, n)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
     
     # output
    #Enter a prime number (p): 7
#Enter another prime number (q): 5

#Public Key: (5, 35)
#Private Key: (5, 35)

#Enter a number to encrypt (should be < 35): 58
#Encrypted message: 18
#Decrypted message: 23