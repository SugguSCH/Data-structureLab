import random
import string #ASCII

class RandomizedCaesarCipher:
    """Class for Caesar cipher encryption and decryption."""
    
    def __init__(self): #อ่านเสมอ
        original = list(string.ascii_uppercase) 
        print("defualt alphabet: ", original)
        shuffled = original[:]  # จับมันเท่ากันทุกตัว
        random.shuffle(shuffled)  # เเล้วก็สุ่มตัวอักษรสลับกันไปหมด
        print("Shuffled alphabet sucessfull: ", shuffled)
        self._forward = dict(zip(original, shuffled))  #สร้าง dict โดย zip : จับคู่ key(Original) : value(Shuffled)
        print("Dictionary alphabet Encrypt: ", self._forward)
        self._backward = {value : key for key, value in self._forward.items()}
        print("Dictionary alphabet Decrypt: ", self._backward)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():  # ใช้เฉพาะตัวพิมพ์ใหญ่
                msg[k] = code.get(msg[k], msg[k])  # แปลงเฉพาะอักษร A-Z
        return ''.join(msg)

# Example usage:        
cipher = RandomizedCaesarCipher()
message = input("Tell your Sentence: ")
coded = cipher.encrypt(message.upper())
decoded = cipher.decrypt(coded.upper())
print("Original Message:", message)
print("Encrypted Message:", coded)
print("Decrypted Message:", decoded)
