#Если в функцию передается кортеж, то посчитаь длину всех его слов
#Если список, то посичтать кол-во букв и чисел в нем
#Число- кол-во нечетных цифр
#Строка- кол-во букв
#Сделать проверку ос всеми этими случаями

some_list1 = ('cat', 'place','dog','keyboard')
some_list2 = ['1' , '3' ,'hello' , '4.55' , '77' , 'world']
some_list3 = 'hello world'


def some_data(n):
    if type(n) == tuple:
        for i in some_list1:
            tup=len(i)
            return (f'слово: {i}, его длинна: {tup}')
    elif type(n) == list:
        sp1 = 0
        sp2 = 0
        for y in some_list2:
            if y.isdigit():
                sp1 += 1
            elif y.isalpha():
                sp2 += 1
        return (f'sumalpha{sp2}, sumdigit{sp1}')
    elif type(n) == str:
        sp3 = 0
        for i in some_list3:
            if i.isalpha():
                sp3+=1
        return sp3

print(some_data(some_list3))







