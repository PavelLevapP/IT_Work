#есть массив состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины
#а после слов цифры в порядке возрастания
sopme_list= ['hello', 'nice', 'sleep','phenomen', '13','7','56']
sopme_list2 = []
sopme_list3 = []

for i in sopme_list:
    if i.isalpha():
        sopme_list2.append(i)
        sopme_list2 = sorted(sopme_list2, key=len)

    elif i.isdigit():
        sopme_list3.append(int(i))
        sopme_list3.sort()

sopme_list2 = str(sopme_list2)
sopme_list3 = str(sopme_list3)

# print(sopme_list2, sopme_list3)

pol = open('example.txt', 'w')
pol.write(sopme_list2)
pol.write(sopme_list3)



















