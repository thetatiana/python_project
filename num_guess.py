import random
print ('Привет! Поиграем? Попробуй угадать число, которое я загадал!')
print ('Введи через enter диапазон чисел, в которых стоит загадать число: ')
x = int(input())
y = int(input())
num = random.randint(x, y)
guess = input('Загадал :) Введи свою догадку: ')
less = ['Многовато будет, попробуй еще: ', 'Попробуй чуть меньше: ', 'Слишком много, попробуй другое число: ', 'Чуть-чуть меньше: ', 'Возьми число поменьше: ', 'Понизь планку: ']
more = ['Маловато будет, попробуй еще: ', 'Попробуй чуть больше: ', 'Слишком мало, попробуй другое число: ', 'Чуть-чуть больше: ', 'Возьми число побольше: ', 'Повысь планку: ']
while int(guess) != num:
    if int(guess) > num:
        guess = input(random.choice(less))
    else:
        guess = input(random.choice(more))
if int(guess) == num:
    print('Молодец, ты угадал число! Сыграем еще?')

