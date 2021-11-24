# Triple DES converted in Python
import pyDes, base64

def encrypt3DES(message,key):
	cipher = pyDes.triple_des(key, pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
	return base64.b64encode(cipher.encrypt(message)).decode('ascii')

def decrypt3DES(message,key):
	cipher = pyDes.triple_des(key, pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
	return cipher.decrypt(base64.b64decode(message.encode('ascii'))).decode('ascii')