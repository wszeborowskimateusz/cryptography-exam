import math

alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

alphabet_with_space = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ "

def decipher_cezar(cipher):
    plain = ""
    for c in cipher:
        if c in alphabet:
            index = (alphabet.find(c) - 3) % len(alphabet)
            plain += alphabet[index]
        else:
            plain += c
    return plain

def decipher_one_time_code(cipher, key):
    plain = ""
    for i, c in enumerate(cipher):
        if c in alphabet:
            index = (alphabet.find(c) - alphabet.find(key[i])) % len(alphabet)
            plain += alphabet[index]
        else:
            plain += c

    return plain

def decipher_plotkowy(cipher, h):
    l = len(cipher)
    t = [["_" for _ in range(l)] for _ in range(h)]
    row = [i for i in range(h)]
    for i in range(h-2, 0, -1):
        row.append(i)
    
    cipher_index = 0
    
    while cipher_index < l:
        for i in row:
            t[i][cipher_index] = "*"
            cipher_index += 1

    cipher_index = 0
    for i in range(h):
        for j in range(l):
            if t[i][j] == "*":
                t[i][j] = cipher[cipher_index]
                cipher_index += 1                

    plain = ""
    for i in range(l):
        for j in range(h):
            if t[j][i] != "_":
                plain += t[j][i]
    return plain

def decipher_kwadratowy(cipher, w):
    subciphers = w * [""]
    index = 0
    for c in cipher:
        subciphers[index] += c
        index = (index + 1) % w

    index = 0
    sub_index = 0
    sub_index_start = 0
    elem_count = 0
    item_skip = 0
    y_index = 0
    plain = ""
    while elem_count < len(cipher):
        for i in range(w):
            if elem_count < len(cipher):
                plain += subciphers[sub_index][i + item_skip]
                elem_count += 1
        y_index += 1
        if(y_index >= w):
            y_index = 0
            item_skip += w
        sub_index = (sub_index + 1) % w
    return plain

def decipher_kolumnowy(cipher, key):
    col_count = len(key)
    col_height = math.ceil(len(cipher) / col_count)
    subciphers = col_count * [""]
    if len(cipher) % col_count != 0:
        # We have some columns that are not full
        key_index = 0
        cipher_index = 0
        items_to_take = col_height
        amount_of_not_full_columns = len(cipher) % col_count 
        while(cipher_index < len(cipher)):
            if alphabet.find(key[key_index]) >= amount_of_not_full_columns:
                # Last amount_of_not_full_columns are not full
                items_to_take = col_height - 1
            else:
                items_to_take = col_height
            for i in range(items_to_take):
                subciphers[key_index] += cipher[cipher_index]
                cipher_index += 1
            key_index += 1
        print(subciphers)
    else:
        col_index = 0
        cipher_index = 0
        while col_index < col_count:
            for _ in range(col_height):
                subciphers[col_index] += cipher[cipher_index]
                cipher_index += 1
            col_index += 1
    
    reversed_sub_sciphers = col_count * [""]
    key_index = 0
    for i in range(col_count):
        reversed_sub_sciphers[alphabet.find(key[key_index])] += subciphers[key_index]
        key_index += 1
    plain = ""
    for i in range(col_height):
        for j in range(col_count):
            if(i < len(reversed_sub_sciphers[j])):
                plain += reversed_sub_sciphers[j][i]
    return plain

def sum_words(word1, word2):
    # Words should be the same size
    result = ""
    for index, c in enumerate(word1):
        if word1[index] in alphabet_with_space and word2[index] in alphabet_with_space:
            result += alphabet_with_space[(alphabet_with_space.find(word1[index])\
                 + alphabet_with_space.find(word2[index])) % len(alphabet_with_space)]
        else:
            result += c

    return result

def subtract_words(word1, word2):
    # Words should be the same size
    result = ""
    for index, c in enumerate(word1):
        if word1[index] in alphabet_with_space and word2[index] in alphabet_with_space:
            result += alphabet_with_space[(alphabet.find(word1[index]) \
                - alphabet_with_space.find(word2[index])) % len(alphabet_with_space)]
        else:
            result += c
    return result

def decipher_feistel(cipher, keys, n_rounds, f):
    plain = cipher
    for i in range(n_rounds):
        plain_1 = plain[0:len(plain)//2]
        plain_2 = plain[len(plain)//2:len(plain)]

        plain_final_2 = plain_1
        plain_final_1 = subtract_words(plain_2, f(plain_1, keys[n_rounds - i - 1])) 

        plain = plain_final_1 + plain_final_2
    return plain


# print(decipher_cezar("WGÓ UAŻIT ÓLG ACSGZÓLC DGASLGEAGPUWZC"))
# print(decipher_one_time_code("TĘO UĄĄLX ÓŁŻB LOIĄURPMBZVAKQQ UĘA SUKŹFA ENXKMGN PRBLGG",\
#      "AĄB CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT UVW XYZŹŻA ĄBCĆDEĘ FGHIJK"))

# print(decipher_plotkowy("SROWN   TŻOZF ŁTOYZAYBŁJŻWSAOYNŚIYPK NYU RTC", 3))

# print(decipher_kwadratowy("SFKZRWY ADTYRO AWNAWYZA YNJE KSTŻTAE CRMIZAEOWTŚYNÓMKÓ", 3))
# print(decipher_kolumnowy("RROAFGAPYEB ZWZMSOCY NIZMMLSEU WRLTRTOSEEKEIM JPAU ", "JIHGFĘEDĆCBĄA"))
# print(decipher_feistel("QASTOHŁYPŻÓŃŻEŁPVRĘMĘQEGUĘŹ VŹJOMĆUÓŁCJXSBRQEĆKOTĘSDOXMF",\
#     4 * ["AĄB CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT UVW XYZŹŻA ĄBCĆDEĘ FGHIJK"]\
#          + ["BZP CĆDEĘ FGHI JKLŁMNŃOÓPQRSŚT TBV XYZŹŻA ĄBCĆDEĘ FGHIJK"], \
#              5, lambda c, k: sum_words(c, k)))