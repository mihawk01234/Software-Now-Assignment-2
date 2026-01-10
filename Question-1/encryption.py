#encryption of the text file

def encrypt_file(shift1, shift2):
    # Open the original text file and read its content
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    encrypted_text = ""

    for ch in text:

        # Encryption rules for lowercase letters
        if ch.islower():
            if 'a' <= ch <= 'm':
                encrypted_text += chr((ord(ch) - ord('a') + shift1 * shift2) % 26 + ord('a'))
            elif 'n' <= ch <= 'z':
                encrypted_text += chr((ord(ch) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
            else:
                encrypted_text += ch

        # Encryption rules for uppercase letters
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                encrypted_text += chr((ord(ch) - ord('A') - shift1) % 26 + ord('A'))
            elif 'N' <= ch <= 'Z':
                encrypted_text += chr((ord(ch) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))
            else:
                encrypted_text += ch
        else:
            encrypted_text += ch

    # Write encrypted content to a new file
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
        
