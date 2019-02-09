from SymmetricCiphers.GCDandInverse.GCD_Inverse import invers



def findtranspose(matri, r, c):
    transposematri = [[0 for col in range(c)] for row in range(r)]
    rn = 0
    cn = 0
    for row in matri:
        for col in row:
            transposematri[cn][rn] = col
            cn += 1
        cn = 0
        rn += 1
    return transposematri


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]



def matrixofminors(matri, r, c):
    matrixminor = [[0 for col in range(c)] for row in range(r)]
    cofactorvalue = 1
    
    for i in range(r):
        for j in range(c):
            minorm = getMatrixMinor(matri, i, j)
            matrixminor[i][j] = (minorm[0][0] * minorm[1][1] - minorm[0][1] * minorm[1][0]) * cofactorvalue
            cofactorvalue *= -1

    return matrixminor
    


def finddeterminant(matri, r, c):
    determinant = 0
    signchange = 1
    for i in range(c):
        minorm = getMatrixMinor(matri, 0, i)
        determinant += ((matri[0][i]) * (minorm[0][0] * minorm[1][1] - minorm[0][1] * minorm[1][0])) * signchange
        signchange *= -1
    return determinant

def multiplymatrixbynumberandmod(matrix_minors, number, r, c):
    for i in range(r):
        for j in range(c):
            matrix_minors[i][j] = (matrix_minors[i][j] * number) % 26
    return matrix_minors



def FindInverse(keymatrix):   
    # keymatrix = [[1, 0, 2],
            #  [0, 1, 3],
            #  [1, 0, 5]
            # ]
    deter = finddeterminant(keymatrix, 3, 3)
    if deter == 0:
        return -1

    
    keytranspose = findtranspose(keymatrix, 3, 3)
    matrix_minors = matrixofminors(keytranspose, 3, 3)
    
    number = invers(deter, 26)

    if (abs(number[0]) <= abs(number[1])):
        number = number[0]
    else:
        number = number[1]

    matrix_minors = multiplymatrixbynumberandmod(matrix_minors, number, 3, 3)
    return matrix_minors