#1) сделайте кортеж с цифрами от 0 до 9 и посчитайте сумму
#2) выведите статистику частности букв в котреже
#long_word = (т, т а и и а и и и т т а а и и и и и т и )
#3) допишите скрипт для расчета средней температуры
#Постарайтесь посчитать количетсво дней на основе week_temp
#Так наш скипр может работать с данными за любой период
#week_temp = (26,29,34,32,28,23)
#sum_temp =
#days =
#mean_temp = sum_temp/days
# print(int(mean_temp))


# sam_numb = (0,1,2,3,4,5,6,7,8,9)
# print(sum(sam_numb))
#2) 2 варианта
long_word = ('t','t','a','i','i','a','i','i','i','t','t','a','a','i','i','i','i','i','t','i')
# long_word_set = set(long_word)
# diferent = len(long_word) - len(long_word_set)
# print(f'буквы повоторяются в кортеже {diferent} раз')

for i in set(long_word):
    print(f'{i}-{long_word.count(i)}')


#
# print(f'буква {i} повторяется {spisok} раз')

# week_temp = (26,29,34,32,28,23)
# sum_temp = (sum(week_temp))
# days = len(week_temp)
# mean_temp = sum_temp/days
# print((int(mean_temp)))

