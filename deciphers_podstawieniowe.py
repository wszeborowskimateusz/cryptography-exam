alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

def decipher_przesuwajacy(cipher, k):
    plain = ""
    for c in cipher:
        if c in alphabet:
            plain += alphabet[(alphabet.find(c) - k) % len(alphabet)]      
        else:
            plain += c
    return plain

def decipher_vigenere(cipher, k):
    plain = ""
    key_index = 0
    for c in cipher:
        if key_index >= len(k):
            key_index = 0
        if c in alphabet:
            plain += alphabet[(alphabet.find(c) - alphabet.find(k[key_index])) % len(alphabet)]
            key_index += 1
        else:
            plain += c

    return plain

print(decipher_przesuwajacy("TŻŹHŚ␣DFŻBŚB␣LFTV␣RŚŻŹŁNBĘFŃ␣TŻŹHŚW␣RŚŻFTWYBLCDFIP", 2))
print(decipher_vigenere("TĘO␣SŹŹFS␣LEŚV␣PÓĘOCOY␣EP␣SŹŹFSW␣Z␣LPDĘŃ␣JĘĘNÓŚAŹPWZŃ", "AĄB"))