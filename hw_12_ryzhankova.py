

def my_list(p):
    if type(p) == tuple:
        print('слов', len(p))
    elif type(p) == list:
        print('букв', len(list(filter(lambda x: type(x) == str, p))), 'чисел', len(list(filter(lambda x: type(x) in (int, float), p))))
    elif type(p) == str:
        print('букв', len(p))
    elif type(p)==int:
        k = 0
        for i in str (p):
            if int (i) % 2 != 0:
                k+= 1
        print(f'нечетных цифр {k}')

my_list((1, 2, 3))
my_list([1, 2, 3, 'a', 'b', 'c'])
my_list('abcd')
my_list(13574)
my_list({1: 2})


