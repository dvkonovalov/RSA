print('Вы находитесь в программе шифра RSA! '
      '\nПеред началом работы поестите открытый текств  файл open_text.txt, а шифртекст в ciphertext.txt.'
      '\nВыберите необходимое действие:\n1 - выполнить шифрование сообщения'
      '\n2 - выполнить расшифрование сообщения(владелец ключевой пары)'
      '\n3 - Сгенерировать ключевую пару')
choice = int(input('Выбор - '))
if (choice == 1):
    import rsa_encrypt
elif (choice == 2):
    import rsa_decrypt
elif (choice == 3):
    import generation_key
