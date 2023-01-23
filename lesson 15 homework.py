import json
#Пользователь будет вводить название и стоимость своей покупки за день, до тех пор
#пока он не напишет СТОП. Ваша задача записать это в Json файл в формате
#{название: яблоко,
#стоимость:200}



with open( 'data.json', 'w', encoding = 'UTF-8' ) as file:
    pokupki_1 = []
    pokupki_2 = []
    while True:
        kluch = input('введите наименование покупки')
        znach = input('введите стоимость покупки')
        pokupki_1.append(kluch)
        pokupki_2.append(znach)
        if kluch == 'стоп' or znach == 'стоп':
            break

    slov = dict(zip(pokupki_1, pokupki_2))
    key = 'стоп'
    if key in slov:
        del slov[key]
    json.dump(slov, file, ensure_ascii=False)

with open( 'data.json', encoding = 'UTF-8' ) as file:
    slov = json.load(file)
    for i in slov:
        print(f'стоимость {i}:{slov[i]}$')








