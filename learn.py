# a = 10
# b = 5
# print(a + b)
# print(a - b)

# from turtle import *
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# print('Я нарисовал квадрат!')

# # Переменные
# run = 5
# print(run)

# name = 'Yaroslav'
# print(name)

# run = 10
# print(run)

# name = run
# print(run, name)

# run = 7
# print(run, name)

# # Типы данных
# # apple = input('Enter number of apples')
# # print(apple + '1') #Текст+текст

# # apple1 = input('Enter number of apples')
# # print(int(apple1) + 1) #Число+число

# #Вычмсления
# ants = 5
# spiders = 70
# bug = ants + spiders
# print(bug)
# ants = 100
# spiders = 100
# print(bug)

# #Строки
# a = 'run'
# b = ' Пришельцы прилетели!'
# c = a + b + ' war'
# print(c)
# len(c)

# #Нумерация символов
# d = 'Harry Potter'
# d[4]
# d[6:12]
# d[:5]
# d[6:]

# print('Привет!\'Как\' дела?') #\ - экранирование.

# #Ввод и вывод
# name = input('Как тебя зовут?')
# print('Привет,', name, sep=('\n'))

# old = input('Сколько тебе лет?')
# print('Мне,',old,'лет', sep=('-')) 

# #Принятие решений
# toys = 10
# toys == 1

# #Ветвление
# a = int(input('введите знчение a'))
# b = int(input('введите знчение b'))
# deyst = input('+-*/')
# if deyst == '+':
#     c = a + b
# elif deyst == '-':
#     c = a - b
# elif deyst == '*':
#     c = a * b
# elif deyst == '/':
#     c = a / b
# else:
#     c = 'Ошибка!!!'
# print('Результат,', c)

# Циклы в Python
# from turtle import *
# # forward(100)
# # right(120)
# # forward(100)
# # right(120)
# # forward(100)
# # right(120)
# # print('Я нарисовал треугольник!')

# for i in range(3):
#     forward(100)
#     right(120)

# for i in range(3, 14, 5): # от, до, шаг
#     print(i, end=' ') # end=' ' - вывести в строку.

# for i in range(3): # повторить три раза, начиная с 0.
#     print(i, end=' ') # end=' ' - вывести в строку.

# for i in range(10, 0, -1):
#     print(i, end=' ') # end=' ' - вывести в строку.

# Вложенные циклы
# n = 3
# for a in range(1, n + 1): #Повторяет заданное количество раз.
#     for b in range(1, n + 1):
#         print(a, '*', b, '=', b * a)

# answer = 'да'
# while answer == 'да': #Повторяет, пока не будет выполнено условие.
#     answer = input('Пойдёшь плавать?')
#     print('Я? ', answer)
# print('Ну тогда я один пойду.')

# # Выход из цикла
# score = 0
# table = 7
# for i in range(1, 13): 
#     print('Сколько будет', i, '*', table)
#     guess = input()
#     if guess == 'стоп':
#         print('Поздравляю, вы бездарь!')
#         break #Выйти из цикла.
#     if guess == 'не знаю':
#         print('Жаль! Перехожу к следующему вопросу!')
#         continue #Пропустить шаг, не выходя из цикла.
#     ans = i * table
#     if int(guess) == ans:
#         print('Правильно!')
#         score = score + 1
#     else:
#         print('Это не правильный ответ.', ans)
# print('Урок окончен!')
# print('Вы набрали', score, 'очков!')
# if score>6:
#     print('Молодец!')
# else:
#     print('Потренируйся ещё!') 

#Списки
# family = ['Папа', 'Мама', 'Ярослав', 'Ростислав', 'Пломбир(кот)']
# # for i in family:
# #     print('Привет,', i)
# print(family[4])


# family_grandfather = ['Дедушка', 'Бабушка', 'Инна', 'Людмила', 'Мейджер', 'Пауль', 'Муза', 'Ника']

# na_dache = family + family_grandfather
# print(na_dache)
# for i in na_dache:
#     print('Привет,', i)

food = [['Конфеты', 'Щоколадка', 'Пицца'], ['Борщ', 'Броколи', 'Сельдерей']]
# print(food)
print(food[0])
# print(food[1])
print(food[1][1])




