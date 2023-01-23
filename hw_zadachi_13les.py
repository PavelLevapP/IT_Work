letters = {'1':'.,?!:','2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz','0':' '}
phrase = (input("Введите фразу: ")).lower()
for s in phrase:    # перебор по символам введеной фразы
    for key in letters: # перебор элементов словаря
        if s in letters[key]:    # ищем вхождение символа в элементе
            for x in letters[key]: # перебор по найденному набору символов
                if x == s:
                    print(key, end='')
                    break
                else:
                    print(key, end='')

def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))
s = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
print("Выпрямленный список: ", flatten(s))