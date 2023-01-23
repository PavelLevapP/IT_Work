import json  # Задача №10 (С вывододом результата в json файл)


def phone_buttons(dictionary, line):
    button_list = []  # список из вводимых кнопок телефона
    line = line.upper()  # перевод в верхний регистр
    for letter in line:  # итерация по строке
        for key, value in dictionary.items():  # итерация по ключам и значениям словаря
            if letter in value:  # проверка на наличие буквы(символа) в списке значения словаря
                button_list.append(key * (dictionary[key].index(letter) + 1))  # добавление в список значения
    return "".join(button_list)  # переводим список в строку


convertible_line = 'Hello, World!'
phone_dictionary = {'0': ' ', '1': ('.', ',', '?', '!', ':'), '2': ('A', 'B', 'C'), '3': ('D', 'E', 'F'),
                    '4': ('G', 'H', 'I'), '5': ('J', 'K', 'L'), '6': ('M', 'N', 'O'), '7': ('P', 'Q', 'R', 'S'),
                    '8': ('T', 'U', 'V'), '9': ('W', 'X', 'Y', 'Z')}
print(type(phone_dictionary.values()))
with open('phone_buttons.json', 'w') as file:
    json.dump(phone_buttons(phone_dictionary, convertible_line), file)
print(f'* Задача №10. Ответ в файле: phone_buttons.json *')


# def alignment_list(data):  # Задача №11 (С вывододом результата в json файл)
#     if not data and isinstance(data, list):  # проверяем является ли список пустым
#         return data  # возвращаем пустой список
#     elif isinstance(data[0], list):   # является ли первый элемент списка data списком
#         l_1, l_2 = data[0], data[1:]  # 1ый элемент списка data; остальные элементы списка data
#         return alignment_list(l_1) + alignment_list(l_2)  # возвращаем результат
#     elif not isinstance(data[0], list):  # не является ли первый элемент списка data списком
#         l_1, l_2 = data[:1], data[1:]  # 1ый элемент списка data; остальные элементы списка data
#         return l_1 + alignment_list(l_2)
#
#
# data_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# with open('alignment_list.json', 'w') as file:
#     json.dump(alignment_list(data_list), file)
# print(f'* Задача №11. Ответ в файле: alignment_list.json *')
