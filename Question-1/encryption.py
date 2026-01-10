#file handles encryption

def _shift_in_half(ch, base, shift, direction, half_size=13):
    """Shift a character within its 13-letter half."""
    pos = ord(ch) - ord(base)
    if direction == "forward":
        new_pos = (pos + shift) % half_size
    else:
        new_pos = (pos - shift) % half_size
    return chr(ord(base) + new_pos)


def encrypt_char(ch, shift1, shift2):
    # Lowercase
    if 'a' <= ch <= 'm':  
        return _shift_in_half(ch, 'a', shift1 * shift2, "forward")
    if 'n' <= ch <= 'z':  
        return _shift_in_half(ch, 'n', shift1 + shift2, "backward")

    # Uppercase
    if 'A' <= ch <= 'M':  
        return _shift_in_half(ch, 'A', shift1, "backward")
    if 'N' <= ch <= 'Z': 
        return _shift_in_half(ch, 'N', shift2 ** 2, "forward")

 
    return ch


def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = "".join(encrypt_char(ch, shift1, shift2) for ch in text)

    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted)
