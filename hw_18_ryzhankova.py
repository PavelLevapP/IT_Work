# Класс Tomato:
# 1. Ȅоздайте класс Tomato
# 2. Ȅоздайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Ȅоздайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1)
# _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Ȅоздайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Ȅоздайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# 1. Ȅоздайте класс TomatoBush
# 2. ȁпределите метод __init__(), который будет принимать в качестве параметра количество томатов и на его
# основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри
# динамического свойства tomatoes.
# 3. Ȅоздайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап
# созревания
# 4. Ȅоздайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Ȅоздайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# 1. Ȅоздайте класс Gardener
# 2. Ȅоздайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name -
# передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является
# protected
# 3. Ȅоздайте метод work(), который заставляет садовника работать, что позволяет растению становиться
# более зрелым
# 4. Ȅоздайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# 5. Ȅоздайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.



class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
    when the fruit is a mature green and
    then allowed to ripen off the vine.
    This prevents splitting or bruising
    and allows for a measure of control over the ripening process.''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

    

  # ====================================================



class Human:

    # Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    # Статический метод
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money!')

    # Приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    small_house = SmallHouse(8_500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(5_000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(20_000)
    alexander.buy_house(small_house, 5)
    alexander.info()

