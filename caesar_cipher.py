"""
Alexander Stepanov (c) 2017
Кодирование/декодирование текстовых строк шифром Цезаря

Шифр Цезаря — это вид шифра подстановки, в котором каждый символ
в открытом тексте заменяется символом, находящимся на некотором
постоянном числе позиций левее или правее него в алфавите.
Например, в шифре со сдвигом вправо на 3, А была бы заменена
на Г, Б станет Д, и так далее.

https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F

Проверить работоспособность алгоритма можно здесь:
http://planetcalc.ru/1434/
"""

eng_abc = 'abcdefghijklmnopqrstuvwxyz'
ENG_ABC = eng_abc.upper()
rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RUS_ABC = rus_abc.upper()
len_eng_abc = len(eng_abc)
len_rus_abc = len(rus_abc)

def caesar_enc(line, offset):
    """
    Кодирование строки шифром Цезаря
    (эта же функция применяется для дешифрации с обратным (отрицательным) смещением,
    т.е. если кодируем со смещением 10, то декодируем со смещением -10)
    :param line: Исходная строка для преобразования шифром Цезаря
    :param offset: смещение для кодирования (0 - оставить без преобразования)
                   смещение может быть как положительным, так и отрицательным,
                   кроме того, смещение может быть больше чем количество символов
                   в алфавите (в данном случае корректное смещение будет вычислено
                   автоматически, причем отдельно для русского и английского алфавитов)
    :return: Измененная строка, полученная из исходной
    """
    if not offset:
        return line
    result = ''

    for char in line:
        if (char in eng_abc) or (char in ENG_ABC):
            if char in eng_abc:
                current_abc = eng_abc
            else:
                current_abc = ENG_ABC
            abc_position = current_abc.find(char) + offset
            if abc_position >= len_eng_abc:
                abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
            if abc_position <= -len_eng_abc:
                abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
            char = str(current_abc[abc_position])
        elif (char in rus_abc) or (char in RUS_ABC):
            if char in rus_abc:
                current_abc = rus_abc
            else:
                current_abc = RUS_ABC
            abc_position = current_abc.find(char) + offset
            if abc_position >= len_rus_abc:
                abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
            if abc_position <= -len_rus_abc:
                abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
            char = str(current_abc[abc_position])

        result += char
    return result

def caesar_dec(line, offset):
    """
    Дещифрация строки зашифрованной шифром Цезаря
    :param line: исходная строка
    :param offset: смещение (то же самое, что было использовано при шифрации)
    :return: декодированная строка
    """
    return caesar_enc(line, -offset)


# Тесты
if __name__ == '__main__':
    tst = 'Проверка шифра Цезаря! One, two, three... Some magic :)'
    print(tst)
    tst_enc = caesar_enc(tst, 100)
    print(tst_enc)
    tst_dec = caesar_dec(tst_enc, 100)
    print(tst_dec)


    #st = 'Зижцодыы юегчя: швцъывым ёележеддеще цщыдизишц Шябиеж Щцвыдияде я ыще зсд, Щжыщщя Шя.'
    #st = 'ЭЙИБЯА ОЫЁЕИ: "ГЕЭДЕ, Х ЕЗИЦШВФ ИЫЧХ ЗЫЧЫ?" БЕОГЦЖ!'
    st = 'Яртпцв, Дтэбфр т Ъощбх!'
    for x in range(1,32):
        print('({0}) {1}=>{2}'.format(x, st, caesar_dec(st, x)))