#pylint: disable=all

# SHA-256 Hashing using hashlib
# Reference: https://docs.python.org/3/library/hashlib.html

import hashlib
import time


def sha256_hash(filename):
    try:
        with open(filename, "rb") as f:
            data = f.read()

        start = time.time()
        sha_hash = hashlib.sha256(data).hexdigest()
        end = time.time()

        print(f"SHA-256 Hash: {sha_hash}")
        print(f"Hashing time: {end - start:.6f} seconds")

    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")
