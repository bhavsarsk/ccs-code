from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_example():
    key = get_random_bytes(8)  # DES key must be 8 bytes
    data = b"Secret Msg"

    # Encryption
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, DES.block_size))
    print("DES Encrypted:", ciphertext)

    # Decryption
    decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
    plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)
    print("DES Decrypted:", plaintext.decode())

des_example()