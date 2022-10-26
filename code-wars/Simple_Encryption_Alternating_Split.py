def decrypt(e_text, n):
    if e_text == "" or n <= 0:
        return e_text
    p = e_text
    x = [ i for i in range(len(p)) if i%2!=0 ] + [ i for i in range(len(p)) if i%2==0 ]
    for _ in range(n):
        q = ["*"]*len(p)
        for i,j in zip(x,p):
            q[i] = j
        p = "".join(q)
    return p


def encrypt(e_text, n):
    if e_text == "" or n <= 0:
        return e_text
    p = e_text
    for _ in range(n):
        e,o = [],[]
        for i,j in enumerate(p):
            if i % 2 == 0:
                e.append(j)
            else:
                o.append(j)
        p = "".join(o+e)
    return p


print(encrypt("This is a test!", 0) == "This is a test!")
print(encrypt("This is a test!", 1) == "hsi  etTi sats!")
print(encrypt("This is a test!", 2) == "s eT ashi tist!")
print(encrypt("This is a test!", 3) == " Tah itse sits!")
print(encrypt("This is a test!", 4) == "This is a test!")
print(encrypt("This is a test!", -1) == "This is a test!")
print(encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig")

print(decrypt("This is a test!", 0) == "This is a test!")
print(decrypt("hsi  etTi sats!", 1) == "This is a test!")
print(decrypt("s eT ashi tist!", 2) == "This is a test!")
print(decrypt(" Tah itse sits!", 3) == "This is a test!")
print(decrypt("This is a test!", 4) == "This is a test!")
print(decrypt("This is a test!", -1) == "This is a test!")
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!")

print(encrypt("", 0) == "")
print(decrypt("", 0) == "")
print(encrypt(None, 0) == None)
print(decrypt(None, 0) == None)
