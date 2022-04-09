import requests

def xor(a,b):
	a = bytes.fromhex(a)
	b = bytes.fromhex(b)
	return bytes(i ^ j for i,j in zip(a,b))
        
cipher = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
cipher = cipher.json()['ciphertext']
# print(cipher)

iv = cipher[:32]
cipher1 = cipher[32:64]
cipher2 = cipher[64:96]

decrypt1 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher1 + '/')
decrypt1 = decrypt1.json()['plaintext']
# print(decrypt1)
decrypt1 = xor(decrypt1,iv)

decrypt2 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher2 + '/')
decrypt2 = decrypt2.json()['plaintext']
# print(decrypt2)
decrypt2 = xor(decrypt2,cipher1)

print(decrypt1+decrypt2)
