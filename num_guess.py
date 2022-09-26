import random
print ('Привет! Поиграем? Попробуй угадать число, которое я загадал!')
print ('Введи через enter диапазон чисел, в которых стоит загадать число: ')
x = int(input())
y = int(input())
num = random.randint(x, y)
guess = input('Загадал :) Введи свою догадку: ')

while int(guess) != num:
    if int(guess) > num:
        guess = input('Попробуй чуть меньше: ')
    else:
        guess = input('Попробуй чуть больше: ')
if int(guess) == num:
    print('Молодец, ты угадал число! Сыграем еще?')

