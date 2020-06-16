from modulo import euler, nwd, euler2
from extended_euclides import solve_equation

def find_key(p, q, fi):
    # Fi from https://www.alpertron.com.ar/ECM.HTM
    n = p * q
    e = 2
    while True:
        if nwd(e, fi) == 1:
            break
        e += 1

    d = solve_equation(e, 1, fi)
    return n, e, d

def find_key_carmichael(p, q, lambda_):
    # Lambda from Wolphram alfa: CarmichaelLambda(x)
    n = p * q
    e = 2
    while True:
        if nwd(e, lambda_) == 1:
            break
        e += 1

    d = solve_equation(e, 1, lambda_)
    return n, e, d

def find_key_version_2(p, q, lambda_):
    # Lambda from Wolphram alfa: CarmichaelLambda(x)
    n = p * q
    e = 2
    while True:
        if nwd(e, lambda_) == 1:
            break
        e += 1

    dp = solve_equation(e, 1, p - 1)
    dq = solve_equation(e, 1, q - 1)
    qi = solve_equation(q, 1, p)
    return n, e, dp, dq, qi

def encrypt_rsa(n, e, m):
    return pow(m, e, n)

def decrypt_rsa(n, d, m):
    return pow(m, d, n)

def decrypt_rsa_version_2(p, q, dp, dq, qi, m):
    m1 = pow(m, dp, p)
    m2 = pow(m, dq, q)
    h = ((m1 - m2) * qi) % p
    return m2 + q * h

def solve_rsa(p, q, fi, lambda_, number_to_encrypt):
    fi = (p-1) * (q-1)
    # Euler
    print("-------------------------------------------------------------------")
    print("Euler")
    n, e, d = find_key(p, q, fi)
    print(f"Found key is: \nn: {n}, \ne: {e}, \nd: {d}")
    encrypted = encrypt_rsa(n, e, number_to_encrypt)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt_rsa(n, d, encrypted)}")
    print("-------------------------------------------------------------------")

    # Carmichael
    print("-------------------------------------------------------------------")
    print("Carmichael")
    n_c, e_c, d_c = find_key_carmichael(p, q, lambda_)
    print(f"Found key is: \nn: {n_c}, \ne: {e_c}, \nd: {d_c}")
    encrypted_c = encrypt_rsa(n_c, e_c, number_to_encrypt)
    print(f"Encrypted Carmichael: {encrypted_c}")
    print(f"Decrypted: {decrypt_rsa(n_c, d_c, encrypted_c)}")
    print("-------------------------------------------------------------------")

    # Version 2
    print("-------------------------------------------------------------------")
    print("Version 2")
    n2, e2, dp, dq, qi = find_key_version_2(p, q, lambda_)
    print(f"Found key is \nn: {n2}, \ne: {e2}, \ndp: {dp}, \ndq: {dq}, \nqi: {qi}")
    encrypted_c = encrypt_rsa(n_c, e_c, number_to_encrypt)
    print(f"Encrypted Version 2: {encrypted_c}")
    print(f"Decrypted: {decrypt_rsa(n_c, d_c, encrypted_c)}")


solve_rsa(2045101337, 1217384479, 2489674622383462608, 1244837311191731304, 1482490597098018112)