alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, key1, key2):
    result = ""
    for symbol in message:
        y = (int(key1) * alphabet.index(symbol) + int(key2)) % 26
        result += alphabet[y]
    return result


def decrypt(text, key1, key2):
    result = ""
    for symbol in text:
        x = ((alphabet.index(symbol) - int(key2)) * pow(int(key1), 11)) % 26
        result += alphabet[x]
    return result


print("Вы хотите расшифровать или зашифровать сообщение? Нажмите соответственно 'd'-decrypt или 'e'-encrypt")
u = input()
print('Введите ключи. Первый ключ должен быть равен одному из этих чисел: 1,3,5,7,9,1,15,17,19,21,23,25')
print('Первый ключ: ')
a = input()
print('Второй ключ: ')
b = input()
print('Введите сообщение: ')
mainMessage = input()
if u == 'e':
    print('Зашифрованное сообщение: ', encrypt(mainMessage, a, b))
elif u == 'd':
    print('Расшифрованное сообщение: ', decrypt(mainMessage, a, b))
