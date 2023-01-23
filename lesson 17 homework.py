# Два метода в классе, один принемает в себя либо строку либо число
# Если я передаю строку, то смотрим:
# если произведение галсных и согласных букв меньше или равно длине слова,
# выводить все галсные иначе согласные
# если число то произведение суммы четных цифр на длину числа
# Длину строки и числа искать во втором методе






class Indetifi:
    sum_str = input('введите число либо строку')
    sum_str = sum_str.lower()
    glasn = 0
    soglasn = 0
    lok = []
    chisl = []
    prois_chisl = 0
    glasn_kol = []
    sogl_kol = []
    def proverka(self):
        if self.sum_str.isalpha():
            for i in self.sum_str:
                if i in 'aeiouy':
                    self.glasn_kol.append(i)
                    self.glasn+=1
                else:
                    self.sogl_kol.append(i)
                    self.soglasn+=1
            return self.glasn, self.soglasn
        elif self.sum_str.isdigit():
            self.sum_str = tuple(self.sum_str)
            for i in self.sum_str:
                i = int(i)
                self.lok.append(i)
            for i in self.lok:
                if i%2 == 0:
                    self.chisl.append(i)
            for i in self.chisl:
                self.prois_chisl+=i
            return self.prois_chisl * len(self.sum_str)
    def dlin(self):
        self.sum_str = len(self.sum_str)
        self.prois_chisl = self.prois_chisl * self.sum_str
        if self.glasn * self.soglasn <= self.sum_str:
            return self.glasn_kol
        else:
            return self.sogl_kol






indet  = Indetifi()
print(indet.proverka())
print(indet.dlin())











