class String_or_number:
    vowel_list = []  # список гласных
    consonant_list = []  # список согласных
    count_even_numbers = 0  # счетчик четных цифр

    def __init__(self):  # вводимый элемент
        self.value = input('Введите слово или число: ')

    def __len__(self):  # метод вычесления длины строки либо длины числа
        return len(self.value)

    def operation_string_or_number(self):  # метод операций с вводимым элементом
        if self.value.isalpha():   # определение принадлежности к алфавитным символам вводимого элемента
            for letter in self.value:  # итерация по слову
                if letter.lower() in 'aeiouyаеёиоуэюя':  # определение гласной буквы
                    self.vowel_list.append(letter)  # добавление в список гласных
                else:
                    self.consonant_list.append(letter)  # добавление в список согласных
            if len(self.vowel_list) * len(self.consonant_list) <= len(str_or_num):  # гласные * согласные <= длины слова
                return f"Cогласные буквы: {''.join(self.consonant_list)}"
            else:
                return f"Гласные буквы: {''.join(self.vowel_list)}"
        elif self.value.isdigit():  # определение цифрового значения вводимого элемента
            for k in self.value:  # итерация по числу
                if int(k) % 2 == 0:  # проверка на чётность
                    self.count_even_numbers += int(k)  # сумма четных цифр
            return f"Произведение суммы чётных цифр и длинны числа: {self.count_even_numbers * len(str_or_num)}"


str_or_num = String_or_number()
print(str_or_num.operation_string_or_number())
