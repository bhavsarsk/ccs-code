from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_example():
    key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes
    data = b"Secret Message"

    # Encryption
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    print("AES Encrypted:", ciphertext)

    # Decryption
    decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
    plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print("AES Decrypted:", plaintext.decode())

aes_example()