#file handles decryption and verification of files

def decrypt_file(shift1, shift2):
    # Open encrypted file and read content
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    decrypted_text = ""
    for ch in text:

        # Decryption rules for lowercase letters
        if ch.islower():
            if 'a' <= ch <= 'm':
                decrypted_text += chr((ord(ch) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
            elif 'n' <= ch <= 'z':
                decrypted_text += chr((ord(ch) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
            else:
                decrypted_text += ch

        # Decryption rules for uppercase letters
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                decrypted_text += chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))
            elif 'N' <= ch <= 'Z':
                decrypted_text += chr((ord(ch) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))
            else:
                decrypted_text += ch

        else:
            decrypted_text += ch

    # Write decrypted content to file
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)


def verify_decryption():
    # Read original file
    with open("raw_text.txt", "r", encoding="utf-8") as f1:
        original = f1.read()

    # Read decrypted file
    with open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    # Compare both files
    if original == decrypted:
        print(" Decryption Successful: Files match")
    else:
        print(" Decryption Failed: Files do not match")
