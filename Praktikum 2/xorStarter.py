string = "label"
integer = 13

unicode = [ord(i) for i in string]
binary = [13 ^ j for j in unicode]
finalString = ''.join(chr(k) for k in binary)

flag = "crypto{" + finalString + "}"

print(flag)
