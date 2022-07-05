def is_valid_IP(strng):
    if strng == "":
        return False
    ip = strng.split(".")
    if len(ip) != 4:
        return False
    for i in ip:
        try:
            if len(i) > 3:
                return False

            if 0<=int(i)<=255:
                continue
            else:
                return False
        except:
            return False
    return True


print(is_valid_IP('12.255.56.1'),     True)
print(is_valid_IP(''),                False)
print(is_valid_IP('abc.def.ghi.jkl'), False)
print(is_valid_IP('123.456.789.0'),   False)
print(is_valid_IP('12.34.56'),        False)
print(is_valid_IP('12.34.56 .1'),     False)
print(is_valid_IP('12.34.56.-1'),     False)
print(is_valid_IP('123.045.067.089'), False)
print(is_valid_IP('127.1.1.0'),        True)
print(is_valid_IP('0.0.0.0'),          True)
print(is_valid_IP('0.34.82.53'),       True)
print(is_valid_IP('192.168.1.300'),   False)