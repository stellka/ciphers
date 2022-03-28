from re import findall

alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,")
MatrixLength = 2
MatrixMod = len(alpha)
MatrixSquare = MatrixLength * MatrixLength

# Проверка условий на ошибки
def checkErrors(key):
    if len(key) != MatrixSquare:
        return "Error: len(key) != %d" % MatrixSquare
    elif not getDeter(trixMatrix(key)):
        return "Error: det(Key) = 0"
    elif not getDeter(trixMatrix(key)) % MatrixMod:
        return "Error: det(Key) mod len(alpha) = 0"
    elif getDeter(trixMatrix(key)) % 29 == 0:
        return "Error: det(Key) mod 29 = 0"
    else:
        return None
    

# Регулярное выражение - 2 символа сообщения
def regular(text):
    template = r".{%d}" % MatrixLength
    return findall(template, text)

# Кодирование символов в матрице
def encode(matrix):
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix

#  умножение матрицы на матрицу
def getProduct22(X,Y):
    a = X[0][0]*Y[0][0] + X[0][1]*Y[1][0]
    b = X[0][0]*Y[0][1] + X[0][1]*Y[1][1]
    c = X[1][0]*Y[0][0] + X[1][1]*Y[1][0]
    d = X[1][0]*Y[0][1] + X[1][1]*Y[1][1]
    matrix = [[a,b],[c,d]]
    return matrix
#  умножение матрицы на строку
def getProduct21(X,Y):
    a = X[0][0]*Y[0] + X[0][1]*Y[1]
    b = X[1][0]*Y[0] + X[1][1]*Y[1]
    matrix = [int(a),int(b)]
    return matrix

# Декодирование чисел в матрице + шифрование
# matrixki - i-тая матрица для кодированиия i-той части сообщения
# matrixPred1,matrixPred2 - последняя и предпоследняя матрица

def code_(matrixm, matrixk1, matrixk2, message=""):
    matrixF = []
    matrixPred1 = matrixk1
    matrixPred2 = matrixk2
    for x in range(len(matrixm)):
        temp = [0 for _ in range(MatrixLength)]
        if x == 0:
            matrixki=matrixk1 
        if x == 1:
            matrixki=matrixk2
        if x >1:
            matrixki=getProduct22(matrixPred1,matrixPred2) 
            matrixPred2=matrixPred1
            matrixPred1=matrixki
        temp=getProduct21(matrixki,matrixm[x]) 
        for i in range(MatrixLength):
            temp[i] = alpha[temp[i] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(string)
    return message

# Декодирование чисел в матрице + дешифрование
# matrixki - i-тая матрица для кодированиия i-той части сообщения
# matrixPred1,matrixPred2 - последняя и предпоследняя матрица

def decode(matrixm, matrixk1, matrixk2, message=""):
    matrixF = []
    matrixPred1 = matrixk1
    matrixPred2 = matrixk2
    for x in range(len(matrixm)):
        temp = [0 for _ in range(MatrixLength)]
        if x == 0:
            matrixki=matrixk1 
        if x == 1:
            matrixki=matrixk2
        if x >1:
            matrixki=getProduct22(matrixPred1,matrixPred2) 
            matrixPred2=matrixPred1
            matrixPred1=matrixki
            
        Inv_matrixki =  getInverseMatr(matrixki)
        temp=getProduct21(Inv_matrixki,matrixm[x]) 
        for i in range(len(temp)):
            temp[i] = alpha[temp[i] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(string)
    return message

# получение мтрицы 2*2
def getInverseMatr(matrix):
    det = getDeter(matrix)
    if (det == 0):
        raise SystemExit
    det = iDet(det)
    a = det*matrix[1][1]
    b = det*(-1)*matrix[0][1]
    c = det*(-1)*matrix[1][0]
    d = det*matrix[0][0]
    return [[a,b],[c,d]]

# Создаёт матрицу по 2 символа
def trixMatrix(text):
    matrix = []
    for two in regular(text):
        matrix.append(list(two))
    return encode(matrix)

# Получение определителя матрицы размера 2*2
def getDeter(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1] )

# Нахождение обратного определителя матрицы
def iDet(det):
    for num in range(MatrixMod):
        if num * det % MatrixMod == 1:
            return num

# Основная функция
def encryptDecrypt(mode, message, key1, key2):
    MatrixMessage, MatrixKey1, MatrixKey2 = trixMatrix(message), trixMatrix(key1),trixMatrix(key2)
    if mode == '1':
        shifrtext = code_(MatrixMessage, MatrixKey1, MatrixKey2 )
    else:
        shifrtext = decode(MatrixMessage, MatrixKey1, MatrixKey2)
    return shifrtext
# 
# main
# 
cryptMode = input("Нажмите 1, если хотите зашифровать сообщение. Нажмите 2, если хотите расшифровать сообщение: ")
if cryptMode not in ['1', '2']:
    print("Error: mode is not Found")
    raise SystemExit

startMessage = input("Write the message: ").upper()
mainKey = input("Write the first key: ").upper()
mainKey2 = input("Write the second key: ").upper()

if checkErrors(mainKey):
    print(checkErrors(mainKey1))
    raise SystemExit
if checkErrors(mainKey2):
    print(checkErrors(mainKey2))
    raise SystemExit
    
for symbol in startMessage:
    if symbol not in alpha:
        startMessage = startMessage.replace(symbol, '')

while len(startMessage) % MatrixLength != 0:
    startMessage += startMessage[-1]

print("Зашифрованное сообщение: ", encryptDecrypt(cryptMode, startMessage, mainKey, mainKey2))