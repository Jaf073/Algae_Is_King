def pass_decrypt(encrypted_password):
    length = len(encrypted_password)
    
    # Reverse the transformation applied during encryption
    decrypted_chars = []
    for i, c in enumerate(encrypted_password):
        # Calculate original character using the inverse of the encryption transformation
        original_char = chr(pow(0xfb, ord(c) - 0x1d, 0xfb) - i + length)
        decrypted_chars.append(original_char)

    # Join the characters to form the decrypted password
    decrypted_password = "".join(decrypted_chars)

    # Remove padding (if any)
    decrypted_password = decrypted_password.lstrip('\xbb')

    return decrypted_password

# Example usage
if __name__ == "__main__":
    #encrypted = pass_hash("¥ÕugÒB×½#¢")  # Assuming this function is defined
    #print("Encrypted:", encrypted)
    
    decrypted = pass_decrypt("¥ÕugÒB×½#¢")
    print("Decrypted:", decrypted)
