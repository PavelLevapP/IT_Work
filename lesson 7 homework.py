# import random
# # Задача 1 По двум введенным пользователем катетам вычислить длину гипотенузы.
#
# gip1 = int(input('введите первый катет'))
# gip2 = int(input('введите второй катет'))
#
# kat = (gip1**2 + gip2**2)
#
# print(kat)


# Задача 2 Вводятся три разных числа. Найти, какое из них является
# средним (больше одного, но меньше другого).

# numeric1 = int(input('Введите первое число'))
# numeric2 = int(input('Введите второе число'))
# numeric3 = int(input('Введите третье число'))
#
# if  numeric3<numeric1<numeric2 or numeric2<numeric1<numeric3:
#     print(f'avg number is {numeric1}')
# elif numeric1<numeric2<numeric3 or numeric3<numeric2<numeric1:
#     print(f'avg number is {numeric2}')
# elif numeric1<numeric3<numeric2 or numeric2<numeric3<numeric1:
#     print(f'avg number is {numeric3}')
# else:
#     print(' you entered the same number')

# Задача 3 Из двух случайных чисел, одно из которых четное, а другое нечетное,
# определить и вывести на экран нечетное число.

# number1 = int(input('введите первое число'))
# number2 = int(input('введите второе число'))
#
# if number1%2==0 and number2%2 ==0:
#     print(f'both numbers are four')
# elif number1%2 != 0 and number2%2 != 0:
#     print(f'both numbers are odd')
# elif number1%2 == 0 and number2%2 != 0:
#     print(f'the odd number is {number2}')
# elif number1%2 != 0 and number2%2 == 0:
#     print(f'the odd number is {number1}')
# else:
#     print('please entered only number ')

#Задание №4
#Сформировать из введенного числа обратное по порядку
#входящих в него цифр и вывести на экран. Например, если
#введено число 3486, то надо вывести число 6843.

# num1 = str(input('enter a number'))
# num1 = int(num1[::-1])
#
# print(num1)


# Задача 5 Найти площади прямоугольника, треугольника или круга.
# примечание: надо ввести фигуру 1-прямоугольник, 2-треугольник,
# 3-круг.

# figure = str(input('enter a number, you can choose 1,2,3 '))
#
# if figure == str(1):
#     figure = 'Прямоугольник'
# elif figure == str(2):
#     figure = 'треугольник'
# elif figure == str(3):
#     figure = 'круг'
# else:
#     print('вы ввели неверную цифру ')

#Задание №6
#Определить существование треугольника по трем сторонам
#Примечание: У треугольника сумма любых двух сторон должна
#быть больше третьей. Иначе две стороны просто "лягут" на третью
#и треугольника не получится.

# num1 = int(input('введите сторону треугольника№1'))
# num2 = int(input('введите сторону треугольника№2'))
# num3 = int(input('введите сторону треугольника№3'))
#
# while num1 + num2 > num3 and num1 + num3 > num2 and num2+num3> num1:
#     print('этот треугольник существует')
#     break
# else:
#     print('такого треугольника не существет')

#Задача 7 Принадлежит ли точка кругу
#Примечание: Если выбрать точку на координатной плоскости,
#то можно увидеть, что проекции ее координат на оси x и y
#являются катетами прямоугольного треугольника. А гипотенуза
#этого прямоугольного треугольника как раз показывает
#расстояние от начала координат до точки. Таким образом, если
#длина гипотенузы будет меньше радиуса круга, то точка будет
#принадлежать кругу; иначе она будет находится за его
#пределами.


# radius = random.randint(1,100)
# kat1 = random.randint(1,10)
# kat2 = random.randint(1,10)
# gip = (kat1**2 + kat2**2)
#
# print(kat1, kat2,radius)
# if gip <= radius:
#     print('точка принадлежит кругу')
# else:
#     print('точка находится за пределами круга')

#Задание №8
#Вводится строка, состоящая из слов, разделенных пробелами.
#Требуется посчитать количество слов в ней.

# line = str(input('введите строку'))
# line = line.split()
# line2 = len(line)
# print(line2)

#Задание №9
#Введите строку c клавиатуры, которая состоит из букв разных
#регистров. Нужно очистить эту строку от всех заглавных букв и
#вывести результат на экран.

# line = str(input('введите строку'))
#
# letter = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# rezalt = ''
# for i in range(len(line)):
#         if line[i] not in letter:
#             rezalt += line[i]
# print(rezalt)


#Задача 10 Задание №10
#Написать программу, которая выводит числа от 0 до 100 на экран,
#пропуская числа кратные 7
#
# for i in range(1,101):
#     if i%7 == 0:
#         print(i)

# Задача 11 Задание №11
# Найти сумму ряда чисел от 1 до 100. Полученный результат
# вывести на экран
# number = 0
# for i in range(1,101):
#     number+=i
# print(number)