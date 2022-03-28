import math
from textwrap import wrap

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def gcd_extended(num1, num2):
    """функция для расширенного алгоритма евклида"""
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)


def text_to_bits(s: str) -> str:
    """функция кодировки символов в двоичный формат ASKII"""
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


# перевод двоичных символов ASKII в нормальные
def text_from_bits(bits, encoding='askii', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or ''


def Bin2Text(text):
    res = [str(int(num, 2)) for num in wrap(text, 8)]
    return ''.join(res)


def pow_mod(x, n, mod):
    """ Выполняет возведение в степень по модулю.

    На вход принимает три числа.
    На выход выдает:
    Результат возведения в ст. по модулю.
    """
    res = 1
    while n != 0:
        if n % 2 != 0:
            res *= x
            res %= mod
            n -= 1
        else:
            x *= x
            x %= mod
            n /= 2
    return res



def chipper(message, p, q, e):
    """основная функция шифрования"""
    n = p * q
    message = list(message)
    message1 = []
    for i in range(len(message)):
        message1.append((str(bin(ord(message[i])))).replace("b", ""))
    message1 = ''.join(message1)
    dot = math.floor(math.log(n, 2)) #на сколько частей делю двоичный код
    while (len(message1) % dot) != 0:
        message1 = '0' + message1
    message2 = [message1[x:x + dot] for x in range(0, len(message1), dot)]
    c = []
    for bink in message2:
        bink1 = int(bink)
        #перевод в десятичную систему счисления
        c.append((pow_mod(bink1, e, n)))
    return c


def dechipper(message = list, p = int, q = int, e = int):
    """функция для расшифрования"""
    n = p * q
    fun_eiler = ((p-1)*(q-1)) % n
    exp_dechipper = gcd_extended(fun_eiler, e)
    c = []
    for i in message:
        c.append(pow_mod(int(i), exp_dechipper[2] % n, n))
    return c


def is_prime(n):
    """ Проверяет число на простоту. """
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


print("1. Хочу зашифровать. 2. Хочу расшифровать.")
t = input()
print('Введите сообщение, которое хотите зашифровать/расшифровать: ')
mess = input()

print('Введите значения простых чисел p and q: ')
pp = int(input())
qq = int(input())

if not(is_prime(pp)) or not(is_prime(qq)):
    print('Error. Введенные числа не являются простыми. Программа не может выполнить дальнейшие действия алгоритма.')
else:
    print('Введите е:')

    ee = int(input())

    if t == "1":
        for bu in (chipper(mess, pp, qq, ee)):
            print(bu, end='')
    elif t == "2":
        print((dechipper([], 29, 41, 3)))
