alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, key):
    result = []
    while len(key) < len(message):
        key += key
    for i in range(len(message)):
        dot = (alphabet.index(message[i]) + alphabet.index(key[i])) % 26
        result.append((alphabet[dot]).upper())
    return result


def decrypt(message, key):
    result1 = []
    while len(key) < len(message):
        key += key
    for i in range(len(message)):
        dot = (alphabet.index(message[i]) - alphabet.index(key[i]) + 26) % 26
        result1.append((alphabet[dot]).upper())
    return result1


def samokey(message, key):
    result2 = []
    key = key + message
    for i in range(len(message)):
        dot = (alphabet.index(message[i]) + alphabet.index(key[i])) % 26
        result2.append((alphabet[dot]).upper())
    return result2


def decrypt_samokey(message, key):
    result3 = []
    key1 = key + message
    recent = alphabet.index(key1[0])
    for i in range(len(message)):
        dot = (alphabet.index(message[i]) - recent + 26) % 26
        recent = dot
        result3.append((alphabet[dot]).upper())
    return result3


def chipper_samokey(message, key):
    result4 = []
    y = key
    for i in range(len(message)):
        if i == 0:
            key = (int(alphabet.index(message[i])) + int(alphabet.index(y))) % 26
            result4.append((alphabet[key]).upper())
        elif i >= 1:
            key = (int(alphabet.index(message[i])) + int(key)) % 26
            result4.append((alphabet[key]).upper())
    return result4


def dechipper_samokey(message, key):
    result5 = []
    y = key
    recent = int(alphabet.index(message[0]))
    for i in range(len(message)):
        if i == 0:
            key1 = (int(alphabet.index(message[i])) - int(alphabet.index(y))) % 26
            result5.append((alphabet[key1]).upper())
        elif i >= 1:
            key1 = (int(alphabet.index(message[i]) - recent + 26)) % 26
            recent = int(alphabet.index(message[i]))
            result5.append((alphabet[key1]).upper())
    return result5


print("1. Хочу зашифровать. 2. Хочу расшифровать.")
enter = input()
print('Подайте на вход сообщение: ')
m = input()
print("Введите ключ: ")
key_print = input()
print(
    "Каким образом будем составлять ключ? 1. повторение короткого лозунга; 2. самоключ Виженера по открытому тексту; 2. самоключ Виженера по шифртексту.")
op = input()
if op == '1':
    if enter == '1':
        print('Зашифрованное сообщение: ', "".join(encrypt(m, key_print)))
    elif enter == '2':
        print('Расшифрованное сообщение: ', "".join(decrypt(m, key_print)))
elif op == '2':
    if enter == '1':
        print('Зашифрованное сообщение: ', "".join(samokey(m, key_print)))
    elif enter == '2':
        print('Расшифрованное сообщение: ', "".join(decrypt_samokey(m, key_print)))
elif op == '3':
    if enter == '1':
        print('Зашифрованное сообщение: ', "".join(chipper_samokey(m, key_print)))
    elif enter == '2':
        print('Зашифрованное сообщение: ', "".join(dechipper_samokey(m, key_print)))
