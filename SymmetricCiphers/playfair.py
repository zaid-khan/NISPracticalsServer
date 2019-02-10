def dum_print2d(keymat):
    for row in keymat:
        for col in row:
            if col == 'I':
                print ('I/J', end=' ')
            else:
                print ('{0}  '.format(col), end=' ')
        print ()



def CreateKeyMatrix(key):
    key_matrix = [['-' for i in range(5)] for i in range(5)]
    
    done_list = [0 for i in range(26)]
    rowc = 0
    colc = 0
    for k in key:
        if k == 'J':
            k = 'I'
        if (done_list[ord(k) - 65] == 0):
            key_matrix[rowc][colc] = k
            colc += 1
            done_list[ord(k) - 65] = 1
            if colc % 5 == 0:
                colc = 0
                rowc += 1
                
    # dum_print2d(key_matrix)

    start_index = 65
    for i in range(start_index, start_index + 26):
        if i == 74:
            continue
        if (done_list[i - start_index] == 0):
            key_matrix[rowc][colc] = chr(i)
            colc += 1
            done_list[i - start_index] = 1
            if colc % 5 == 0:
                colc = 0
                rowc += 1
    return key_matrix
    

def findposition(achar, key_matrix):
    rc = 0
    cc = 0
    for row in key_matrix:
        for col in row:
            if col == achar:
                return rc, cc
            cc += 1
        rc += 1
        cc = 0


        

def decrypt(firstchar, secondchar, key_matrix):
    
    if firstchar == 'J':
        firstchar = 'I'
    if secondchar == 'J':
        secondchar = 'I'

    firstchar_row, firstchar_col = findposition(firstchar, key_matrix)
    secondchar_row, secondchar_col = findposition(secondchar, key_matrix)

    if firstchar_row != secondchar_row and firstchar_col != secondchar_col:
        return key_matrix[firstchar_row][secondchar_col] + key_matrix[secondchar_row][firstchar_col]

    elif firstchar_col == secondchar_col:
        return key_matrix[(firstchar_row - 1) % 5][firstchar_col] + key_matrix[(secondchar_row - 1) % 5][secondchar_col]

    else:
        return key_matrix[firstchar_row][(firstchar_col - 1) % 5] + key_matrix[secondchar_row][(secondchar_col - 1) % 5]




def PlayFairDecrypt(ciphertext, key):
    # key = "MONARCHY"
    # plaintext = 'WE ARE DISCOVERED SAVE YOURSELF'
    key_matrix = CreateKeyMatrix(key)
    dum_print2d(key_matrix)

    
    c = 1
    plaintext = ""

    while c <= len(ciphertext):
        plaintext += decrypt(ciphertext[c - 1], ciphertext[c], key_matrix)
        print (plaintext)
        c += 2

    return plaintext
    

