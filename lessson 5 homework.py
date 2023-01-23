import random
# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х
# соответственно цифры от одного до 10 отвечают за номера, а от 1
# до 2 за цвет (1 красный, 2 черный)
# Пользователю дается 5 попыток угадать номер и цвет (Прим
# введения с клавиатуры: 3 красный). В случае неудачи вывести
# на экран правильную комбинацию


# a = int(random.randint(1,10))
# b = str(random.randint(1,2))
# c = 0
#
# if b == str(1):
#     b = 'red'
# elif b == str(2):
#     b = 'black'
#
# for c in range (6):
#     guess_num = int(input('введите число от 1 до 10'))
#     guess_color = str(input('введите цвет red or black'))
#     c = c+1
#
#     if b != guess_color or a != guess_num:
#         print(f'вы не угалаи')
#     elif c == 6:                                    # Федор, я пока не понимаю почему условие не работает?
#         print('к сожалению попыток не осталось')
#     else:
#         break
#
# if a == int(guess_num) and b == str(guess_color):
#     print('поздравляю вы у угадали')
# elif a != guess_color or b != guess_num:
#     print(f'очень жаль я загадал число {a} и цвет {b}.')
#     # print(type(c))




# a = str(random.randint(1,10))
# b = str(random.randint(1,2))
# c = 0
#
# if b == str(1):
#     b = 'red'
# elif b == str(2):
#     b = 'black'
#
# for c in range (6):
#     guess_som = str(input('введите число от 1 до 10 и цвет (Black or Red) через пробел'))
#     guess_som = guess_som.split(' ')
#
#     if  guess_som[0] != a or guess_som[1] != b:
#         print('вы не угадали')
#     else:
#         break
# if guess_som[0] == a and guess_som[1] == b:
#     print('поздравляю вы у угадали')
# elif a != guess_som or b != guess_som:
#     print(f'очень жаль я загадал число {a} и цвет {b}.')



a = str(random.randint(1,10))
b = str(random.randint(1,2))


if b == str(1):
    b = 'red'
elif b == str(2):
    b = 'black'
c = 0
guesstaken = True
while guesstaken:
    guess_som = str(input('введите число от 1 до 10 и цвет (Black or Red) через пробел'))
    guess_som = guess_som.split(' ')

    if  guess_som[0] == a and guess_som[1] == b:
        print('вы угадали')
    else:
        print('попытайтесь еще раз')
    if c == 5:
        print(f'попытки закончились, было загаданно число {a} и цвет {b}.')
        break
    c += 1



