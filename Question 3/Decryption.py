def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower() and shifted < ord('a'):
                shifted += 26
            elif char.isupper() and shifted < ord('A'):
                shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Encrypted code
encrypted_code = '''
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
qrs cebprff_ahzoref():
    tybony_tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbjr(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
    erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)
qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr
zbqvsl_qvpg(5)
qrs hcqngr_tybony():
    tybony_tybony_inevnoyr
    tybony_inevnoyr += 10
sbe v va enatr(5):
    cevag(v)
    v += 1
vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
    cevag("5 abhaq va gur qvpgvbanell!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
'''

# Decrypting the code
key = 13  # ROT13 cipher
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
