# class Human:
#     default_name = 'No name'
#     default_age = 0
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         return f"Name -> {self.name} \n" \
#                f"Age -> {self.age} \n " \
#                f"Money -> {self.__money} \n" \
#                f"House -> {self.__house}"
#
#     def buy_house(self, house, discount):
#         price = int(house.final_price(discount))
#         if self.__money >= price:
#             self.__make_deal(house, price)
#             return f'ДОМ КУПЛЕН! [оставшиеся средства на счету: {self.__money}$]'
#         else:
#             return f'Недостаточно средств! Стоимость дома: {price}$ [оставшиеся средства на счету: {self.__money}$]'
#
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house
#
#     @staticmethod
#     def default_info():
#         return f'Default name = {Human.default_name}, ' \
#                f'Default age = {Human.default_age}'
#
#     def earn_money(self, amount):
#         self.__money += amount
#         return f'* Зачисление на счёт {amount}$ [оставшиеся средства на счету: {self.__money}$]'
#
#
# class House(Human):
#     def __init__(self, area, price):
#         super().__init__()
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price * (100-discount) / 100
#         return final_price
#
#
# class SmallHouse(House):
#     default_area = 40
#
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)
#
#
# if __name__ == '__main__':
#
#     pavel = Human('Pavel', 26)
#     small_house = SmallHouse(2000)
#     print(pavel.buy_house(small_house, 5))
#     print(pavel.earn_money(2500))
#     print(pavel.buy_house(small_house, 5))
#     print(pavel.earn_money(5000))
#     print(pavel.buy_house(small_house, 5))
'---------------------------------------------------------------------------------------'

# Задача 2

class Tomato:
    states = {0:'зародыш',1:'лепесток',2:'зачаток',3:'томат'}
    tomat = []
    def __init__(self,index):
        self._index = index
        self._state = 0

    def grou(self):
        self.states = self.states[self.states.index(self.states)+1]

    def is_ripe(self):
        if self.tomat == self.states[-1]:
            return 'томат, созрел'
        else:
            return 'томат, не созрел'
class TomatoBush(Tomato):

    def __init__(self,quantity,index):
        super.__init__(index)
        self.tomatoes = [Tomato(i) for i in range(quantity)]

    def grow_all(self):
        for i in self.tomatoes:
            self._state[i] = self.states[self.states.index(self.states)+1]

    def all_are_ripe(self):
        for i in self.tomatoes:
            if self._state[i] == self.states[-1]:
                return 'все томаты созрели'
            else:
                return 'не все томаты созрели'

    def give_away_all(self):
        for i in self.tomatoes:
            if self._state[i] == self.states[-1]:
                self.tomatoes.remove(i)



class Gardener(Tomato):
    def __init__(self,name,index):
        super.__init__(index)
        self.name = name
        self._plant = self._plant

    def work(self):
        self._plant = self.states[self.states.index(self.states)+1]
        return f'стадия созревания после работы садовника "{self._plant}"]'

    def harvest(self):
        if self._plant == self.states[-1]:
            return 'можно собирать помидоры'
        else:
            return 'плоды еще не созрели'


    @staticmethod
    def knowledge_base():
        return 'Справка: In case of an incomprehensible result for the harvest, contact the gardener, he will destroy everything)'

if __name__ == '__main__':
    print(Gardener.knowledge_base())

    tomato_bush = TomatoBush(3, 0)
    gardener = Gardener('Эркюль', 2)

    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.harvest())























