import random

SIMPLE_P = 984167
SIMPLE_Q = 500921


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


def alg_evklida(a, b):
    """
    Нахождение НОД двух чисел
    :param a: первое число
    :param b: второе число
    :return: НОД введенных двух чисел
    """
    if (b>a):
        a,b = b,a
    while (b!=0):
        r = a%b
        a = b
        b = r
    return a

def alg_evklida_revers_element(a, b):
    """
    Вычисляет обратный элемент x для сравнения a*x = 1*(mod b)
    :param a: число
    :param b: число
    :return: обратный элемент
    """
    if a<b:
        a,b = b,a
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while (b>0):
        q = a//b
        r = a-q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2
    y = y2
    return y2

def is_simple(chislo):
    """
    Проеряет является число простым или нет по малой теореме Ферма
    :param chislo: Число
    :return: True - если число простое и False в ином случае
    """
    count = 1000
    mas_chisel = []
    if (chislo<1000):
        count = chislo//2
    for i in range(count):
        a = random.randint(2, chislo-1)
        while (a in mas_chisel):
            a = random.randint(2, chislo-1)
        if (calc_step(a, chislo-1, chislo)!=1):
            return False
        mas_chisel.append(a)
    return True

def write_key(close_key, open_key):
    """
    Записывает закрытый и открытый ключи в соответствующие файлы
    :param close_key: закрытый ключ
    :param open_key: открытый ключ
    """
    file = open('close_key.txt', 'w')
    file.write(str(close_key))
    file.close()
    file = open('open_key.txt', 'w')
    file.write(str(open_key[0]) + ' ' + str(open_key[1]))
    file.close()

def gen_key():
    choice = int(input('Откуда будут взяты простые числа для модуля алгоритма: \n1 - введены вручную\n2 - программные\nВыбор - '))
    p = SIMPLE_P
    q = SIMPLE_Q
    if (choice==1):
        p, q = map(int, input('Введите простые числа (числа должны быть различны и |p-q| должно быть большим числом) через пробел - ').split())
    while (is_simple(p) and is_simple(q))!=True:
        print('Взятые числа не простые!!!')
        p, q = map(int, input(
            'Введите простые числа (числа должны быть различны и |p-q| должно быть большим числом) через пробел - ').split())
    n = p*q
    fi = (p-1)*(q-1)
    choice = int(input('Как будет задана экспонента зашифрования: \n1 - вручную\n2 - программно\nВыбор - '))
    e = 0
    temp = 0
    print('Модуль алгоритма - ', n)
    if (choice==1):
        e = int(input('e = '))
        while (alg_evklida(e,fi)!=1):
            e = int(input('Введеная экспонента зашифрования не является взаимно простой с функцией Эйлера. Введите e снова - '))
    else:
        e = 174067
        print('Экспонента зашифрования - ', e)
    close_key = alg_evklida_revers_element(e, fi)
    close_key = close_key%fi
    print('Экспонента расшифрования - ', close_key)
    print('\n\n\nОткрытый ключ - ', e, n)
    print('Закрытый ключ - ', close_key)
    return close_key, [e, n]



print('Запущена генерация ключей!')
choice = int(input('Ключевая пара будет введена вручную или выработана программно: \n1 - вручную\n2 - сгенерирована\nВыбор - '))
if (choice==1):
    close_key = int(input('Введите закрытый ключ - '))
    open_key = list(map(int, input('Введите пару значений для открытого ключа через пробел - ').split()))
    write_key(close_key, open_key)
elif (choice==2):
    close_key, open_key = gen_key()
    write_key(close_key, open_key)
else:
    print('Введены некорректные данные')

print('\nГенерация ключей завершена!')