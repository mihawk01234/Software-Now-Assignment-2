# main.py

from encryption import encrypt_file
from decryption import decrypt_file, verify_decryption

def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypt_file(shift1, shift2)
    print("Encryption completed.")

    decrypt_file(shift1, shift2)
    print("Decryption completed.")

    verify_decryption()

if __name__ == "__main__":
    main()
