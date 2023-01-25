# class Cardeck:
#     def __iter__(self):
#         self.x = 1
#         return self
#     def __next__(self):
#         if self.x <=52:
#             y = self.x
#             self.x += 1
#             return y
#         else:
#             raise StopIteration
#
# classinstance = Cardeck()
# element = iter(classinstance)
# while True:
#     print(f'{next(element)} Пик')

class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__suits = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__ranks = [*range(2, 11), 'A', 'K', 'J', 'Q']

    def __next__(self):
        if self.index >= 52:
            raise StopIteration
        else:
            suit = self.__suits[self.index // len(self.__ranks)]
            rank = self.__ranks[self.index % len(self.__ranks)]
            self.index += 1
            return f'{rank} {suit}'

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))
