import random
from typing import List, Any, Union


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# функция шифрования по ключу
# text - list символов шифра
# key - list с перестановкой на алфавите
def encrypt(text, key):
    result = []
    for i in range(len(text)):
        result.append(key[alphabet.index(text[i])])

    return result


# Функция дешифрования по ключу
# code - list символов шифра
# key - list с перестановкой на алфавите
def decrypt(code, key):
    result = []
    for i in range(len(code)):
        result.append(alphabet[key.index(code[i])])

    return result


print("Вы хотите зашифровать или расшифровать текст? Нажмите соответственно 'd'-decrypt или 'e' - encrypt")

vvod = input()

print("Введите ключ(латинский алфавит в произвольном порядке): ")
key_print = input()

if vvod == 'e':
    print('Подайте на вход открытый текст: ')
    text1 = input()
    print('Зашифрованный текст: ', "".join(encrypt(text1, key_print.split())))
elif vvod == 'd':
    print('Подайте на вход зашифрованное сообщение: ')
    code1 = input()
    print('Расшифрованный текст: ', "".join(decrypt(code1, key_print.split())))
