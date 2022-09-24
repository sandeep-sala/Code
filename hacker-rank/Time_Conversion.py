def timeConversion(s):
    k = s[:2]
    if s[-2:] == 'PM':
        k = '12' if s[:2] == '12' else str(12 + int(k))
    else:
        k = '00' if s[:2] == '12' else str(s[:2])
    return str(k)+s[2:-2]

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)