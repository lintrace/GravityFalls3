"""
Шифр Атбаш
"""
# ВНИМАНИЕ! Под Линукс возник интересный момент связанный
# с использованием кодировки UTF-8 и отличным порядком следования
# символов от кодировки Windows-1251, в частности нарушен порядок букв Е и Ё
# из-за этого неправильно работало шифрование и дешифрование между платформами!
# Трюк со словарями это способ выкрутиться из этого положения
# и придти к универсальному решению для любых кодировок
eng_abc = 'abcdefghijklmnopqrstuvwxyz'
rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

table = {}
for i in eng_abc:
    table[i]=eng_abc[len(eng_abc) - eng_abc.find(i)-1]
    table[i.upper()] = eng_abc[len(eng_abc) - eng_abc.find(i) - 1].upper()
for i in rus_abc:
    table[i]=rus_abc[len(rus_abc) - rus_abc.find(i)-1]
    table[i.upper()] = rus_abc[len(rus_abc) - rus_abc.find(i) - 1].upper()

#print(table)

def atbash_encdec(line):
    '''
    Кодирование и декодирование строки шифром Атбаш.
    Функция одна, так как процесс зеркально обратимый.
    Первым проходом - шифрование, вторым - дещифрация
    :param line: исходная строка
    :return: зашифрованная (или декодированная) строка
    '''
    result = ''
    for char in line:
        if char in table:
            result += table[char]
        else:
            result += char
    return result



# Тесты

if __name__ == '__main__':
    result = atbash_encdec('Тестовая строка, которая будет зашифрована шифром Атбаш')
    print(result)
    print(atbash_encdec(result))
