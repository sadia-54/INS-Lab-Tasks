#pylint: disable=all

# AES Encryption and Decryption with file I/O
# Reference: https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time
import os


def aes_encrypt_decrypt():
    input_file = input("Enter filename to encrypt (e.g., input.txt): ")

    if not os.path.exists(input_file):
        print("File not found.")
        return

    with open(input_file, 'rb') as f:
        data = f.read()

    # --- AES 128-bit ECB ---
    key_128 = get_random_bytes(16)
    with open("aes_key_128.bin", "wb") as f:
        f.write(key_128)

    cipher = AES.new(key_128, AES.MODE_ECB)
    padded = data + b' ' * (16 - len(data) % 16)
    start = time.time()
    encrypted = cipher.encrypt(padded)
    end = time.time()

    with open("aes_128_ecb_encrypted.bin", "wb") as f:
        f.write(encrypted)
    print(
        f"AES-128 ECB encryption done in {end - start:.6f} seconds → aes_128_ecb_encrypted.bin")

    # Decrypt from file
    with open("aes_128_ecb_encrypted.bin", "rb") as f:
        encrypted = f.read()

    cipher_dec = AES.new(key_128, AES.MODE_ECB)
    decrypted = cipher_dec.decrypt(encrypted).rstrip()
    print("Decrypted AES-128 ECB data:", decrypted[:100], "\n")

    # --- AES 256-bit CFB ---
    key_256 = get_random_bytes(32)
    iv = get_random_bytes(16)
    with open("aes_key_256.bin", "wb") as f:
        f.write(key_256)

    cipher = AES.new(key_256, AES.MODE_CFB, iv=iv)
    start = time.time()
    encrypted = cipher.encrypt(data)
    end = time.time()

    with open("aes_256_cfb_encrypted.bin", "wb") as f:
        f.write(iv + encrypted)
    print(
        f"AES-256 CFB encryption done in {end - start:.6f} seconds → aes_256_cfb_encrypted.bin")

    # Decrypt from file
    with open("aes_256_cfb_encrypted.bin", "rb") as f:
        iv = f.read(16)
        encrypted = f.read()

    cipher_dec = AES.new(key_256, AES.MODE_CFB, iv=iv)
    decrypted = cipher_dec.decrypt(encrypted)
    print("Decrypted AES-256 CFB data:", decrypted[:100], "\n")
