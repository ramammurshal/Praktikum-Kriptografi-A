import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# 1. Get chipertext from server
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("Ciphertext:", ciphertext)

# 2. Send chipertext to decrypt function server
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("Plaintext:", plaintext)

# 3. Convert hex string plain text to get the flag
print("Flag:", bytearray.fromhex(plaintext).decode())
