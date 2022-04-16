import requests

ciphertext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json()['ciphertext']

iv = ciphertext_hex[:32]
print("Initialization vector: ", iv)

ciphertext = ciphertext_hex[32:]
print("Ciphertext: ", ciphertext)

plaintext = requests.get('http://aes.cryptohack.org/symmetry/encrypt/'+ciphertext+'/'+iv+'/').json()['ciphertext']
flag = bytes.fromhex(plaintext)
print("Flag: ", flag)
