#pylint: disable=all

# Cryptography Task Menu
# Combines AES, RSA, Signature, Hashing, and Graph plotting
# Each algorithm is in its own module file

from aes import aes_encrypt_decrypt
from rsa import rsa_encrypt_decrypt
from rsaSignature import rsa_signature
from shaHashing import sha256_hash
from timeGraph import plot_time_graph

if __name__ == "__main__":
    while True:
        print("\nSelect operation:")
        print("1. AES Encryption/Decryption")
        print("2. RSA Encryption/Decryption")
        print("3. RSA Digital Signature")
        print("4. SHA-256 Hashing")
        print("5. Plot Execution Time Graph")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            aes_encrypt_decrypt()
        elif choice == '2':
            rsa_encrypt_decrypt()
        elif choice == '3':
            rsa_signature()
        elif choice == '4':
            filename = input("Enter filename to hash: ")
            sha256_hash(filename)
        elif choice == '5':
            plot_time_graph()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
