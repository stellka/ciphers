alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def recursion_encrypt(message, key1, key2):
    key1 = key1.split()
    a1 = key1[0]
    b1 = key1[1]
    key2 = key2.split()
    a2 = key2[0]
    b2 = key2[1]
    result = ""
    for i in range(len(message)):
        if i == 0:
            y = (int(a1) * alphabet.index(message[i]) + int(b1)) % 26

        if i == 1:
            y = (int(a2) * alphabet.index(message[i]) + int(b2)) % 26

        if i >= 2:
            keyai = (int(a2) * int(a1)) % 26
            keybi = (int(b1) + int(b2)) % 26
            a1 = a2
            a2 = keyai
            b1 = b2
            b2 = keybi
            y = (int(keyai) * alphabet.index(message[i]) + int(keybi)) % 26

        result += alphabet[y]
    return result


def recursion_decrypt(message, key1, key2):
    key1 = key1.split()
    a1 = key1[0]
    b1 = key1[1]
    key2 = key2.split()
    a2 = key2[0]
    b2 = key2[1]
    result = ""
    for i in range(len(message)):
        if i == 0:
            x = (alphabet.index(message[i]) - int(b1)) * pow(int(a1), 11) % 26
        if i == 1:
            x = (alphabet.index(message[i]) - int(b2)) * pow(int(a2), 11) % 26
        if i >= 2:
            keyai = (int(a2) * int(a1)) % 26
            keybi = (int(b1) + int(b2)) % 26
            a1 = a2
            a2 = keyai
            b1 = b2
            b2 = keybi
            x = ((alphabet.index(message[i]) - int(keybi)) * pow(int(keyai), 11)) % 26

        result += alphabet[x]

    return result


print("Вы хотите зашифровать или расшифровать сообщение? Нажмите соответственно 'd' - decrypt или 'e' - encrypt")
mode = input()
print("Введите сообщение: ")
vvod = input()

print("Введите ключи а1 и b1: ")
print_key1 = input()
print("Введите ключи а2 и b2: ")
print_key2 = input()

if mode == 'e':
    print("Зашифрованное сообщение: ", recursion_encrypt(vvod, print_key1, print_key2))
elif mode == 'd':
    print("Расшифрованное сообщение: ", recursion_decrypt(vvod, print_key1, print_key2))
