alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

def przesuwajacy(plain, k):
    cipher = ""
    for c in plain:
        if c in alphabet:
            cipher += alphabet[(alphabet.find(c) + k) % len(alphabet)]      
        else:
            cipher += c
    return cipher

def vigenere(plain, k):
    cipher = ""
    key_index = 0
    for c in plain:
        if key_index >= len(k):
            key_index = 0
        if c in alphabet:
            cipher += alphabet[(alphabet.find(c) + alphabet.find(k[key_index])) % len(alphabet)]
            key_index += 1
        else:
            cipher += c

    return cipher

# print(przesuwajacy("SZYFR␣CEZARA␣JEST␣PRZYKŁADEM␣SZYFRU␣PRZESUWAJĄCEGO", 2))
print(vigenere("ZDO SNMUBO LTXC YĄS Z JVBBV PŃPŃEEMSÓV AHŹFŚR FVŃŹOO ÓŹ CIJOPFMP ĆDŁLŚ OH ĆCDFG DVKGĆJŃBQ ŃĆŚĄŃMEK IITVCJU DĘ DĆĘV PPYŃYVMDŚĄ ŹJ", "GĄŚN"))