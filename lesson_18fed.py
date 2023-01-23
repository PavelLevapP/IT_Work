






# class Car:
#
#     def __str__(self):
#         return 'This is Car'
#
#     def star(self):
#         print('Запускаем двигатель')
#
# car = Car()
# print(car)
# print(car.__dir__())



# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'Toy_phone')
#         return toy_phone
#
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('My operator is MTS')
#
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
# print(Phone.model_hash('I785'))
# print(Phone.toy_phone('red'))
# my_phone = Phone('red', 'I785')
# print(Phone('red', 'I785').check_sim('MTS'))
# my_phone.check_sim('MTS')


# Класс Human
#
# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и
# age. Для этих параметров задайте значения по умолчанию, используя свойства
# default_name и default_age. В методе __init__() определите четыре свойства:
# публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и
# money.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить
# статические поля default_name и default_age.
# 6. Реализуйте метод earn_money(), увеличивающий значение свойства money.
# class God:
#
#     def miracle(self):
#         return True
#
class Human():

    #наши статические атрибуты
    default_name = 'fiodar'
    default_age = 39

    def __init__(self, name=default_name, age=default_age):
        #тут мы описывыем динамические поля
        #1)Публичные
        self.name = name
        self.age = age
        #2)Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        return f"Name -> {self.name} \n" \
               f"Age -> {self.age} \n " \
               f"Money -> {self.__money} \n" \
               f"House -> {self.__house}"

    @staticmethod
    def default_info():
        return f"Default name => {Human.default_name} \n" \
               f"Default age => {Human.default_age}"

    def earn_money(self, salary):
        self.__money += salary
        return f"Im add same => {salary} $. Now my budget =>  {self.__money}. {self.name}"
#
#
# print(f"1) {Human.default_info()}")
# max = Human('Maxim', 49)
# print(f"2) {max.info()}")
#
# print(f"3) {max.earn_money(100)}")
# print(f"{max.earn_money(500)}")
# print(f"4) {max.info()}")
#
# stas = Human('Stas', 59)
# print(f"5) {stas.info()}")
# print(f"6) {stas.earn_money(100)}")
# print(f"7) {max.earn_money(-600)}")

#Родительский класс
class Phone:
    #наш инициализхатор родительский
    def __init__(self):
        self.is_on = False


    """пользовательский метод. Вкл. телефон"""
    def turn_on(self):
        self.is_on = True

    """пользовательский метод. Звонит телефон, если он включен"""
    def call(self):
        if self.is_on:
            return f"Calling..."

# Подкласс. Унаследованный от родительского
class MobilePhone(Phone):

    #добавим новое свойство в инициализатор
    def __init__(self):
        super().__init__()
        self.battery = 0

    """пользовательский метод. Зарядим телефон на переданное значение"""
    def charge(self, pr):
        self.battery += pr
        return f"We're charging battery up to {pr}. All battery = {self.battery}"

my_mobile_phone = MobilePhone()
print(dir(my_mobile_phone))


class Camera:
    def camera(self):
        pass

class Radio:
    def rafio(self):
        pass

class Phone(Camera, Radio):
    def phone(self):
        pass

print(Phone().__dir__())


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, dis):
        final_price = self._price * (100-dis)
        return f"Discount is => {dis}. Total final_price => {final_price}"

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

class Car:

    def __init__(self, model):
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return f"Год выпуска модели: {self.model}"

car_1 = Car(2019)
print(car_1.getCarModel())

import string
class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return f"In current alphabet => {len(self.letters)} letters"

class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('EN', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return f"{letter} from ENG Alphabet"
        return f"{letter} not from ENG Alphabet"

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return f"Hello! I'm english text"


eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('Q'))
print(eng_alphabet.is_en_letter('Ф'))
print(EngAlphabet.example())