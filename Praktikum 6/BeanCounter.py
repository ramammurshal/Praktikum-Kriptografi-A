import requests
from Crypto.Util.strxor import strxor

response = requests.get('http://aes.cryptohack.org/bean_counter/encrypt/').json()['encrypted']
data = bytes.fromhex(response)
header = bytes.fromhex('89504e470d0a1a0a0000000d49484452')

iv = strxor(header, data[:16])

plaintext = b''
for i in range(0,len(data),16):
	block = data[i:i+16]
	plaintext += strxor(block, iv[0:len(block)])

f=open('bean_counter_flag.png','wb').write(plaintext)
