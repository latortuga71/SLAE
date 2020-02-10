import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
plaintext = b'test'
key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext)
nonce = b64encode(cipher.nonce).decode("utf-8")
ct = b64encode(ciphertext).decode("utf-8")
result = json.dumps({'nonce':nonce,'ciphertext':ct})
print(key)
################ encrypt ########################











######################## decrypt here ##########################3
>>> import json
>>> from base64 import b64decode
>>> from Crypto.Cipher import ChaCha20
>>>
>>> # We assume that the key was somehow securely shared
>>> try:
>>>     b64 = json.loads(json_input)
>>>     nonce = b64decode(b64['nonce'])
>>>     ciphertext = b64decode(b64['ciphertext'])
>>>     cipher = ChaCha20.new(key=key, nonce=nonce)
>>>     plaintext = cipher.decrypt(ciphertext)
>>>     print("The message was " + plaintext)
>>> except ValueError, KeyError:
>>>     print("Incorrect decryption")




############### find how to run shellcode with python ##################
