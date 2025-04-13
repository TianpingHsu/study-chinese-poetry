import sys
sys.path.append("..")
import models.bochk.bochk
import models.protection.encrypt.AESCipher
import models.bochk.bochk

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
    
    @staticmethod
    def make_an_appointment():
        boc = models.bochk.bochk.Bochk()
        boc.continueInput()


