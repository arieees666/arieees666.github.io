import base64

plaintext = open('plain.txt').read()
print(base64.b64decode(plaintext))