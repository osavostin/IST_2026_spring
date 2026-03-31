def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            ciphertext += chr(start + (ord(char) - start + shift) % 26)
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            plaintext += chr(start + (ord(char) - start - shift) % 26)
        else:
            plaintext += char
    return plaintext
