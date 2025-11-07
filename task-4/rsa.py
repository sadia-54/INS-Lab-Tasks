#pylint: disable=all

# RSA Encryption and Decryption with file I/O
# Reference: https://pycryptodome.readthedocs.io/en/latest/src/examples.html

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import os


def rsa_encrypt_decrypt():
    input_file = input("Enter filename to encrypt (e.g., input.txt): ")

    if not os.path.exists(input_file):
        print("File not found.")
        return

    # Generate and save RSA keys
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("rsa_private.pem", "wb") as f:
        f.write(private_key)
    with open("rsa_public.pem", "wb") as f:
        f.write(public_key)

    # Read data
    with open(input_file, "rb") as f:
        data = f.read()

    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

    # Encrypt
    start = time.time()
    # RSA can only encrypt small chunks (≤ key_size/8 - padding)
    encrypted = cipher.encrypt(data[:190])
    end = time.time()

    with open("rsa_encrypted.bin", "wb") as f:
        f.write(encrypted)
    print(
        f"RSA encryption done in {end - start:.6f} seconds → rsa_encrypted.bin")

    # Decrypt
    with open("rsa_encrypted.bin", "rb") as f:
        encrypted = f.read()

    cipher_dec = PKCS1_OAEP.new(RSA.import_key(private_key))
    start = time.time()
    decrypted = cipher_dec.decrypt(encrypted)
    end = time.time()
    print(f"RSA decryption done in {end - start:.6f} seconds")
    print("Decrypted RSA data:", decrypted[:100], "\n")
