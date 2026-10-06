import random
import string

symbols_without_punc = string.ascii_letters + string.digits
symbols = string.ascii_letters*2 + string.digits*2 + string.punctuation

n = input('''1 - Пароль с дополнительными символами
2 - Пароль без дополнительных символов
''')
if n not in '12' :
    print('Неправильный ввод')

elif n == '1':
    length = int(input('Введите длину пароля: '))
    password = ''
    for i in range(length):
        password += random.choice(symbols)

elif n == '2':
    length = int(input('Введите длину пароля: '))
    password = ''
    for i in range(length):
        password += random.choice(symbols_without_punc)

print(f'Ваш пароль: {password}')