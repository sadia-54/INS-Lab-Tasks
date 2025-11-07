#pylint: disable=all

# Plot execution time vs key size for AES and RSA
# References:
# AES - https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# RSA - https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-rsa-keys
# Matplotlib - https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import time
import matplotlib.pyplot as plt


def plot_time_graph():
    aes_key_sizes = [16, 24, 32]  # 128, 192, 256 bits
    rsa_key_sizes = [1024, 2048, 3072, 4096]  # fixed: all >= 1024

    aes_times = []
    rsa_times = []

    data = b"Performance test data!"

    # AES timing
    for key_size in aes_key_sizes:
        key = get_random_bytes(key_size)
        cipher = AES.new(key, AES.MODE_ECB)
        padded = data + b' ' * (16 - len(data) % 16)

        start = time.time()
        cipher.encrypt(padded)
        end = time.time()

        aes_times.append(end - start)

    # RSA timing
    for key_size in rsa_key_sizes:
        key = RSA.generate(key_size)
        public_key = key.publickey()
        cipher = PKCS1_OAEP.new(public_key)

        start = time.time()
        cipher.encrypt(b"Test RSA speed")
        end = time.time()

        rsa_times.append(end - start)

    # Plot graphs
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot([128, 192, 256], aes_times, marker='o', label="AES")
    plt.title('AES Encryption Time vs Key Size')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(rsa_key_sizes, rsa_times, marker='o', label="RSA", color='orange')
    plt.title('RSA Encryption Time vs Key Size')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.tight_layout()
    plt.show()
