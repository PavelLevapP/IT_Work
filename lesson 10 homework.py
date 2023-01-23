#У вас есть словарь, где ключ – название продукта.
#Значение – список, который содержит цену и кол-во
#товара.
#Выведите через ‘’–’’ название – цену – количество.
#С клавиатуры вводите название товара и его кол-во. n –
#выход из программы. Посчитать цену выбранных товаров
#и сколько товаров осталось в изначальном списке.

spisok_znach = [{'количество': 12, 'стоимость': 15.00,}, {'количество': 34, 'стоимость': 81.77,}, {'количество': 22, 'стоимость': 22.7}]
products = ['Milk', 'Meat', 'Bread']
all_in = dict(zip(products,spisok_znach))
print(all_in)
a=1
while a == 1:
    zapros1 = str(input('введите наименование товара'))
    zapros2 = int(input('введите количество товара'))
    zapros1 = zapros1.title()
    if zapros1 in all_in and zapros2 <= all_in[zapros1]['количество'] and zapros1 != 'n':
        ostatok = (all_in[zapros1]['количество'] - zapros2)
        price = float(zapros2) * all_in[zapros1]['стоимость']
        print(f'по запросу:{zapros1}, остаток на складе: {ostatok}, стоимость выбранных товаров составляет: {price}')
    elif zapros1 not in all_in and zapros1 != 'n':
        print('вы ввели несуществующий товар')
    elif zapros1 == 'n':
        break















