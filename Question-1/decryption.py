##file handles decryption and verification of files

def _shift_in_half(ch, base, shift, direction, half_size=13):
    """Shift a character within its 13-letter half."""
    pos = ord(ch) - ord(base)
    if direction == "forward":
        new_pos = (pos + shift) % half_size
    else:
        new_pos = (pos - shift) % half_size
    return chr(ord(base) + new_pos)


def decrypt_char(ch, shift1, shift2):
    # Lowercase
    if 'a' <= ch <= 'm': 
        return _shift_in_half(ch, 'a', shift1 * shift2, "backward")
    if 'n' <= ch <= 'z': 
        return _shift_in_half(ch, 'n', shift1 + shift2, "forward")

    # Uppercase
    if 'A' <= ch <= 'M':
        return _shift_in_half(ch, 'A', shift1, "forward")
    if 'N' <= ch <= 'Z':
        return _shift_in_half(ch, 'N', shift2 ** 2, "backward")

    return ch


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    decrypted = "".join(decrypt_char(ch, shift1, shift2) for ch in text)

    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted)


def verify_decryption():
    with open("raw_text.txt", "r", encoding="utf-8") as f1:
        original = f1.read()

    with open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    if original == decrypted:
        print("Decryption Successful: Files match")
    else:
        print("Decryption Failed: Files do not match")
