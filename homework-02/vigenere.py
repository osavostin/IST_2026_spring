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
    keyword_repeated = ""
    
    # Repeat the keyword to match the length of the plaintext
    while len(keyword_repeated) < len(plaintext):
        keyword_repeated += keyword
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword_repeated[i].upper()) - ord('A')
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shift = ord(keyword_repeated[i].lower()) - ord('a')
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
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
    keyword_repeated = ""
    
    # Repeat the keyword to match the length of the ciphertext
    while len(keyword_repeated) < len(ciphertext):
        keyword_repeated += keyword
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword_repeated[i].upper()) - ord('A')
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                shift = ord(keyword_repeated[i].lower()) - ord('a')
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
    
    return plaintext
