from SymmetricCiphers.GCDandInverse.inversecalculaton import FindInverse


def getKeyMatrix(key, keyMatrix): 
	k = 0
	for i in range(3): 
		for j in range(3): 
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1


def decrypt(cipherVector, plainMatrix, inverseMatrixWithMod):    
    
    for i in range(3):
        for j in range(1):
            plainMatrix[i][j] = 0
            for x in range(3):
                plainMatrix[i][j] += (inverseMatrixWithMod[x][i] *
									cipherVector[x][j])
            plainMatrix[i][j] = plainMatrix[i][j] % 26                



def HillCipherDecrypt(cipher, inverseMatrixWithMod, cipherVector, plainMatrix):
    for i in range(3): 
        cipherVector[i][0] = ord(cipher[i]) % 65

    decrypt(cipherVector, plainMatrix, inverseMatrixWithMod)
	# Generate the encrypted text 
	# from the encrypted vector 
    PlainText = ""


    for i in range(3): 
        PlainText += (chr(plainMatrix[i][0] + 65)) 

	# Finally print the ciphertext 
    return PlainText





def HillCipherDecryptWrapper(ciphertext, key):
    keyMatrix = [[0] * 3 for i in range(3)] 
    
    cipherVector = [[0] for i in range(3)] 

    plainMatrix = [[0] for i in range(3)]

    
    getKeyMatrix(key, keyMatrix) # For Encryption

    inverseMatrixWithMod = FindInverse(keyMatrix)

    if len(ciphertext) <= 0:
        print ('Error. Insufficent length of the cipher text.')
    else:
        ciphertext = [ciphertext[start:start+3] for start in range(0, len(ciphertext), 3)]
    plaintext = ""



    for c in ciphertext:    
        plaintext += HillCipherDecrypt(c, inverseMatrixWithMod, cipherVector, plainMatrix)    
    
    return plaintext

