# number1 = float(input('введите число'))
# number2 = str(input('введите логический оператор'))
# number3 = float(input('введите число'))
#
# def summ(nuber1,number3):
#     return nuber1+number3
# def minus(nuber1,number3):
#     return nuber1-number3
# def umn(nuber1,number3):
#     return nuber1*number3
# def delen(nuber1,number3):
#     return nuber1/number3
# if number3 == 0 and number2 == '/':
#     print('на ноль делить нельзя')
# elif number2 == '*':
#     print(umn(number1,number3))
# elif number2 == '/':
#     print(delen(number1,number3))
# elif number2 == '+':
#     print(summ(number1,number3))
# elif number2 == '-':
#     print(minus(number1,number3))





#Найти площади прямоугольника, треугольника или круга.
#примечание: надо ввести фигуру 1-прямоугольник, 2-треугольник,
#3-круг.

# type_fig = int(input('введите цифру от 1 до 3'))



# def plprym(a=4,b=6):
#     return a*b
# def plkrug (r=3):
#     return 3.14*r**2
# def pltreug (a=7,b=6,r=9,c=2):
#     return r*(a+b+c)*0.5
# if type_fig == 1:
#     print(plprym())
# elif type_fig == 2:
#     print(pltreug())
# elif type_fig == 3:
#     print(plkrug())
# else:
#     print('неверно введены цифры')


a = input('Введите возраст')   # я вроде разобрался с задачей)

try:
    if int(a) >= 18:
        print('ok')
    else:
        print('not ok')
except ValueError:
    print('вы ввели не число')