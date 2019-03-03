#: Open the file, and get only the possible keys
ciphertext = [3,9,13,15,18,7,20,1,4,14,5,21,6,2,17,10,8,16,12,11,19]
file = open('february_14th.txt').read().replace(' ', '').splitlines()[3::2]
plaintext = ''

for i in range(len(ciphertext)):
	plaintext += file[i][ciphertext[i] - 1]

print(plaintext)