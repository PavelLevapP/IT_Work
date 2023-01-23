import  random
import  math

# придумать задачу...
#1)Сколько нужно поставить знаков «плюс» (+) между цифрами числа 987 654 321, чтобы в сумме получилось 99?
# solution:
#print(9+8+7+65+4+3+2+1)
#2) Найти длину окружности если D = 18
# solution:
# P = 3.14
# D = 18
# circumference = int((2*P*D/2))
# print(circumference)
#3) Дан диапазон двух факториалов чисел 4 и 6 соответсвтенно, найти остаток от деления числа (рандомное число в диапазоне факториалов) на число 5
#
# number1 = math.factorial(4)
# number2 = math.factorial(6)
# number3 = random.randint(number1,number2)
# ostatok = math.fmod(number3,5)
# ostatok = int(ostatok)
# print(f'{int(number3 % 5)}')
# print(ostatok)



#
# # задача 1
# aApple = 2
# pApple = 5
# print(f'у Анны было {aApple} яблока, у Пола было {pApple} яблок')
#
# # задача 2
# edje = int(input('введиет длинну ребра'))
# V = (edje**3)
# S = (edje**2)
# print(f'Объем куба равен {V}')
# print(f'Площадь боковой поверхности куба равен {S}')
#
# #задача 3
# dayLUp = 2
# nightLDown = 1
# allDistance = 20
# dayDistance = (dayLUp-nightLDown)
# timeDistance = (allDistance/dayDistance)
# timeDistance = int(timeDistance)
# print(timeDistance)




# list = [1,2,3,4,5,6,7,8,9]
# print(sip)
# sip = random.choice(list)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[1::2])
# print(numbers[-1::2]) #начнет с последнего значения.
# print(numbers[3:-2:2])