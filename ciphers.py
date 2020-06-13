import random

alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

alphabet_with_space = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ "

def cezar(plain):
    cipher = ""
    for c in plain:
        if c in alphabet:
            index = (alphabet.find(c) + 3) % len(alphabet)
            cipher += alphabet[index]
        else:
            cipher += c
    return cipher

def one_time_code(plain, key):
    cipher = ""
    for i, c in enumerate(plain):
        if c in alphabet:
            index = (alphabet.find(c) + alphabet.find(key[i])) % len(alphabet)
            cipher += alphabet[index]
        else:
            cipher += c

    return cipher

def plotkowy(plain, h):
    cipher = ""
    subciphers = h * [""]
    index = 0
    go_down = True
    for c in plain:
        subciphers[index] += c

        if index == 0 and go_down == False:
            go_down = True
        if index == h - 1 and go_down == True:
            go_down = False
        
        if go_down:
            index +=1
        else:
            index -=1
    return "".join(subciphers)

def kwadratowy(plain, w, filler=""):
    if filler == '':
        filler = "".join([random.choice(alphabet) for _ in range(((w * w) - 1))])

    print(f"filler: {filler}")
    subciphers = 3 * [""]
    index = 0
    counter = 0
    for c in plain:
        subciphers[index] += c
        counter += 1
        if counter >= w * w:
            counter = 0
        if counter % w == 0 and index < w:
            index += 1
        if index >= w:
            index = 0

    # Need to fill
    i = 0
    while counter < w * w:
        subciphers[index] += filler[i]
        i+=1
        counter += 1
        if counter % w == 0 and index < w:
            index += 1
        if index >= w:
            index = 0

    cipher = ""
    for x in range(len(subciphers[0])):
        for z in range(w):
            cipher += subciphers[z][x]
    return cipher

def kolumnowy(plain, key):
    decoded_key = [alphabet.find(x) for x in key]
    n = len(key)
    subciphers = []
    x = 0
    y = 0
    subciphers.append("")
    for c in plain:
        if x >= n:
            subciphers.append("")
            x = 0
            y += 1
        x+=1
        subciphers[y] += c
    cipher = ""
    for i in range(n):
        column_index = decoded_key[i]
        for j in range(len(subciphers)):
            if(len(subciphers[j]) > column_index):
                cipher += subciphers[j][column_index]   
    return cipher

def sum_words(word1, word2):
    # Words should be the same size
    result = ""
    for index, c in enumerate(word1):
        if word1[index] in alphabet_with_space and word2[index] in alphabet_with_space:
            result += alphabet_with_space[(alphabet_with_space.find(word1[index]) \
                + alphabet_with_space.find(word2[index])) % len(alphabet_with_space)]
        else:
            result += c

    return result

def feistel(plain, keys, n_rounds, f):
    cipher = plain
    for i in range(n_rounds):
        cipher_1 = cipher[0:len(cipher)//2]
        cipher_2 = cipher[len(cipher)//2:len(cipher)]

        cipher_final_1 = cipher_2
        cipher_final_2 = sum_words(f(cipher_2, keys[i]), cipher_1) 

        cipher = cipher_final_1 + cipher_final_2
    return cipher

# print(plotkowy("SZYFR PŁOTKOWY ZNANY BYŁ JUŻ W STAROŻYTNOŚCI", 3))
# print(cezar("TEN SZYFR NIE ZAPEWNIA BEZPIECZEŃSTWA"))

# print(one_time_code("TEN SZYFR JEST BEZPIECZNIEJSZY ALE WYMAGA DŁUGICH KLUCZY",\
#      "AĄB CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT UVW XYZŹŻA ĄBCĆDEĘ FGHIJK"))

# print(kwadratowy("SZYFR KWADRATOWY NAZYWANY JEST TAKŻE MACIERZOWYM", 3))

# print(kolumnowy("PIERWSZYM PARAMETREM SZYFRU KOLUMNOWEGO JEST LICZBA", "JIHGFĘEDĆCBĄA"))
# print(kolumnowy("TO_JEST_MOJA_UKRYTA_WIADOMOŚĆ", "JIFGHĘEDĆCBĄA"))
print(feistel("TEN SZYFR JEST BEZPIECZNIEJSZY ALE WYMAGA DŁUGICH KLUCZY",\
       4 * ["AĄB CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT UVW XYZŹŻA ĄBCĆDEĘ FGHIJK"]\
         + ["BZP CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT TBV XYZŹŻA ĄBCĆDEĘ FGHIJK"],\
              5, lambda c, k: sum_words(c, k)))