#pylint: disable=all

# RSA Digital Signature using files
# Reference: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os
import time


def rsa_signature():
    input_file = input("Enter filename to sign (e.g., input.txt): ")

    if not os.path.exists(input_file):
        print("File not found.")
        return

    with open(input_file, "rb") as f:
        data = f.read()

    # Generate keys
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("rsa_sig_private.pem", "wb") as f:
        f.write(private_key)
    with open("rsa_sig_public.pem", "wb") as f:
        f.write(public_key)

    h = SHA256.new(data)

    # Sign
    start = time.time()
    signature = pkcs1_15.new(key).sign(h)
    end = time.time()
    with open("signature.bin", "wb") as f:
        f.write(signature)
    print(f"Signature generated in {end - start:.6f} seconds → signature.bin")

    # Verify
    with open("signature.bin", "rb") as f:
        signature = f.read()

    h_verify = SHA256.new(data)
    start = time.time()
    try:
        pkcs1_15.new(RSA.import_key(public_key)).verify(h_verify, signature)
        print("Signature verification successful.")
    except (ValueError, TypeError):
        print("Signature verification failed.")
    end = time.time()
    print(f"Verification time: {end - start:.6f} seconds\n")
