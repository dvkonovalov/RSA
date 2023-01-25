import math

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


file = open('open_key.txt', 'r')
open_key = file.readline()
file.close()
open_key = list(map(int, open_key.split()))
length_block = math.floor(math.log2(open_key[1]))+1
with open('ciphertext.txt', 'r', encoding='ASCII') as file:
    for text in file:
        mas_answer = []
        if (text == ''):
            continue
        shest_text = list(map(str, text.split()))
        bin_text = ''
        for i in shest_text:
            chislo = int(i, 16)
            bin_text += get_bait(chislo)
        c = []
        for i in range(len(bin_text) // length_block):
            c.append(int(bin_text[len(bin_text) - (i + 1) * length_block:len(bin_text) - i * length_block], 2))
        print('Перехваченные значения в строке: ', *c)
        for element in range(len(c)):
            p = calc_step(c[element], open_key[0], open_key[1])
            pr = p
            count = 0

            while (p != c[element]):
                pr = p
                count += 1
                p = calc_step(p, open_key[0], open_key[1])
            print(f'Число {c[element]} возводим в степень {count}. Результат расшифрования {pr}')
            c[element] = pr
        bin_text = ''
        length_block -= 1
        for i in c:
            bin_text = get_bin_fix_length(i, length_block) + bin_text
        text_ret = ''
        for i in range(len(bin_text) // 8):
            chislo = int(bin_text[len(bin_text) - (i + 1) * 8:len(bin_text) - i * 8], 2)
            if (chislo == 0):
                continue
            text_ret = chr(chislo) + text_ret
        mas_answer.append(text_ret)
        print(*mas_answer)

