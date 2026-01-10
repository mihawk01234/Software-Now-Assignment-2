# decryption.py
# This file handles decryption and verification of files

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    decrypted_text = ""

    for ch in text:
        if ch.islower():
            # Reverse of a-m forward (shift1 * shift2)
            if 'a' <= ch <= 'z':
                # Try reversing both rules safely using modulo
                # First half reverse
                test1 = chr((ord(ch) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
                # Second half reverse
                test2 = chr((ord(ch) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))

                # Decide which one falls in correct original range
                if 'a' <= test1 <= 'm':
                    decrypted_text += test1
                else:
                    decrypted_text += test2

        elif ch.isupper():
            # Reverse of A-M backward and N-Z forward
            test1 = chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))
            test2 = chr((ord(ch) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))

            if 'A' <= test1 <= 'M':
                decrypted_text += test1
            else:
                decrypted_text += test2
        else:
            decrypted_text += ch

    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)


def verify_decryption():
    with open("raw_text.txt", "r", encoding="utf-8") as f1:
        original = f1.read()

    with open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    if original == decrypted:
        print("✅ Decryption Successful: Files match")
    else:
        print("❌ Decryption Failed: Files do not match")
