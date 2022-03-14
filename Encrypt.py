class Encryptor:

    def encrypt(self, text, key):
        encrypted_text = ''
        for symb in text:
            encrypted_text += chr(ord(symb) + key)
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = ''
        for symb in text:
            decrypted_text += chr(ord(symb) - key)
        return decrypted_text
