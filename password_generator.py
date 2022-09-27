import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
count = int(input('Сколько паролей сгенерировать?: '))
length = int(input('Какой длины сгенерировать пароль?: '))
whattoinclude = input('Что включить в пароль? Напишите буквы без пробелов: n - цифры, l - буквы в нижнем регистре, u - буквы в верхнем регистре, p - знаки пунктуации: ')
chars = ''
for i in whattoinclude:
    if i == 'n':
        chars += digits
    if i == 'l':
        chars += lowercase_letters
    if i == 'u':
        chars += uppercase_letters
    if i == 'p':
        chars += punctuation
def my_password(length, chars):
    password = ''
    for i in range (length):
        password += random.choice(chars)
    return password
for i in range (count):
    print(my_password(length, chars))
