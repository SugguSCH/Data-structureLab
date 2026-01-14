#from nltk.stem import PorterStemmer
class CaesarCipher:
    """Class for Caesar cipher encryption and decryption."""

    def __init__(self, shift):
        encoder = [None] * 26 
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)  
        self._backward = ''.join(decoder)  

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

    def brute_force_decrypt(secret):
        """ลองทุกคีย์ (0-25) เพื่อถอดรหัส"""
        for shift in range(0,26):  
            cipher = CaesarCipher(shift) 
            decrypted_text = cipher.decrypt(secret)
            print(f"Key {shift}: {decrypted_text}") 


# example use
#ps = PorterStemmer()
cipher = CaesarCipher(0)
message = "WTAAD LDGAS"
encrypted_message = cipher.encrypt(message) 
print(f"Starting Encrypted: {encrypted_message}") #เลขมันไม่ตรงเพราะมันถอยหลัง
print("\nTrying all possible keys:")
CaesarCipher.brute_force_decrypt(encrypted_message)  