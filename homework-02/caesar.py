import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    return encrypt_caesar(ciphertext, -shift)

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    max_matches = -1
    
    for shift in range(26):
        decoded = decrypt_caesar(ciphertext, shift)
        words = decoded.split()
        matches = sum(1 for word in words if word.lower() in dictionary)
        
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
            
    return best_shift
