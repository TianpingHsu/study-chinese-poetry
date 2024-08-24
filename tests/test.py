import sys
sys.path.append("..")
import models.protection.encrypt.AESCipher

class Test:

    def __init__(self):
        return

    @staticmethod
    def encrypt_with_aes(key, plaintext):
        cipher = models.protection.encrypt.AESCipher.AESCipher(key)
        return cipher.encrypt(plaintext)

    @staticmethod
    def decrypt_with_aes(key, cipheredtext):
        cipher = models.protection.encrypt.AESCipher.AESCipher(key)
        return cipher.decrypt(cipheredtext)


