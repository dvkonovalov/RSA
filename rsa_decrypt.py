import math


def calc_step(a,k, n):
    """
    Возводит число a в степень k по модулю n
    :param a: число для возведения в степень
    :param k: стпень числа
    :param n: модуль
    :return: результат операции
    """
    mas_k = bin(k)[2:]
    b= 1
    if (k==0):
        return b
    aa = a
    if (mas_k[-1]=='1'):
        b = a
    for i in range(1, len(mas_k)):
        aa = aa*aa % n
        if (mas_k[len(mas_k) - i -1]=='1'):
            b = (aa*b) % n
    return b


def get_bin_fix_length(chislo, length):
    """
    Получить бинарный вид числа chislo в фиксированной длине length бит
    :param chislo: число в десятичном виде
    :param length: фиксированная длина бит
    :return: резльтат перевода
    """
    chislo = bin(chislo)[2:]
    if (len(chislo) > length):
        chislo = chislo[-length:]
    elif (len(chislo) < length):
        chislo = '0' * (length - len(chislo)) + chislo
    return chislo


def get_bait(chislo):
    """
    Приводит входное число к двоичному 8-битовому виду
    :param chislo: десятичное число, меньшее 256
    :return: двочная строка из 8 бит
    """
    chislo = bin(chislo)[2:]
    if (len(chislo) < 8):
        chislo = '0' * (8 - len(chislo)) + chislo
    elif (len(chislo) > 8):
        chislo = chislo[-8:]
    return chislo


print('Запущена программа расшифрования по шифру RSA')
print('Шифртекст взят из файла ciphertext.txt')
file = open('close_key.txt', 'r')
close_key = file.readline()
file.close()
close_key = int(close_key)
print('Закрытый ключ взят из файла open_key.txt')
print('Открытый ключ взят из файла open_key.txt')
file = open('open_key.txt', 'r')
open_key = file.readline()
file.close()
open_key = list(map(int, open_key.split()))
length_block = math.floor(math.log2(open_key[1]))
mas_answer = []
with open('ciphertext.txt', 'r', encoding='ASCII') as file:
    for text in file:
        if (text == ''):
            continue
        length_block += 1
        shest_text = list(map(str, text.split()))
        bin_text = ''
        for i in shest_text:
            chislo = int(i, 16)
            bin_text += get_bait(chislo)
        c = []
        for i in range(len(bin_text) // length_block):
            c.append(int(bin_text[len(bin_text) - (i + 1) * length_block:len(bin_text) - i * length_block], 2))
        bin_text = ''
        length_block -= 1
        for i in c:
            chislo = calc_step(i, close_key, open_key[1])
            bin_text = get_bin_fix_length(chislo, length_block) + bin_text
        text_ret = ''
        for i in range(len(bin_text) // 8):
            chislo = int(bin_text[len(bin_text) - (i + 1) * 8:len(bin_text) - i * 8], 2)
            if (chislo == 0):
                continue
            text_ret = chr(chislo) + text_ret
        mas_answer.append(text_ret)
file = open('open_text.txt', 'w', encoding='ASCII')
for i in mas_answer:
    file.write(i + '\n')
file.close()
print('Программа успешно закончила работу!')
