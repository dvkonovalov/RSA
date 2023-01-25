import math


def get_bin_code(symbol):
    """
    Функция для получения бинарного вида ASCII символа
    :param symbol: символ, принадлежащий ASCII кодировке
    :return: бинарная строка с 8 битами
    """
    symbol = bin(ord(symbol))[2:]
    if (len(symbol) > 8):
        symbol = symbol[-8:]
    elif (len(symbol) < 8):
        symbol = '0' * (8 - len(symbol)) + symbol
    return symbol

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
    if (len(chislo)>length):
        chislo = chislo[-length:]
    elif (len(chislo)<length):
        chislo = '0'*(length-len(chislo)) + chislo
    return chislo


print('Запущена программа шифрования по шифру RSA')
print('Открытый текст взят из файла open_text.txt')
file = open('open_key.txt', 'r')
open_key = file.readline()
file.close()
open_key = list(map(int, open_key.split()))
print('Открытый ключ для шифрования был взят из файла open_key.txt')
length_block = math.floor(math.log2(open_key[1])) + 1
ciphertext = []
with open('open_text.txt', 'r', encoding='ASCII') as file:
    for stroka in file:
        stroka = stroka.replace('\n', '')
        if stroka=='':
            ciphertext.append('\n')
            continue
        length_block -= 1
        bin_text = ''
        dec_block = []
        for i in stroka:
            bin_text += get_bin_code(i)
        if (len(bin_text) % length_block != 0):
            bin_text = '0' * (length_block - len(bin_text) % length_block) + bin_text
        for i in range(len(bin_text)//length_block):
            dec_block.append(int(bin_text[i*length_block:(i+1)*length_block], 2))
        length_block += 1
        bin_text = ''
        for i in range(len(dec_block)):
            dec_block[i] = calc_step(dec_block[i], open_key[0], open_key[1])
            bin_text += get_bin_fix_length(dec_block[i], length_block)
        if (len(bin_text) % 8 != 0):
            bin_text = '0' * (8 - len(bin_text) % 8) + bin_text
        bytes = []
        for i in range(len(bin_text)//8):
            bytes.append(hex(int(bin_text[i*8:(i+1)*8], 2))[2:])
        ciphertext.append(bytes)
file = open('ciphertext.txt', 'w')
for i in ciphertext:
    file.write(' '.join(i))
    file.write('\n')
file.close()

print('Шифрование успешно завершено!\nРезультат можно увидеть в файле ciphertext.txt')


