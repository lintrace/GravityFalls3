"""
Alexander Stepanov (c) 2017
Кодирование/декодирование текстовых строк шифром Виженера

Шифр Виженера (фр. Chiffre de Vigenère) — метод полиалфавитного
шифрования буквенного текста с использованием ключевого слова.

https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0

The Vigenère cipher is a method of encrypting alphabetic text
by using a series of interwoven Caesar ciphers based on the letters of a keyword.
It is a form of polyalphabetic substitution.
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""

eng_abc = 'abcdefghijklmnopqrstuvwxyz'
ENG_ABC = eng_abc.upper()
rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RUS_ABC = rus_abc.upper()
len_eng_abc = len(eng_abc)
len_rus_abc = len(rus_abc)

def vigenere_enc(line, password, offset=0, neg_pass_offset=False):
    """
    Кодирование строки шифром Виженера
    (эта же функция применяется для дешифрации с обратным (отрицательным) смещением,
    т.е. если кодируем со смещением 10, то декодируем со смещением -10)
    :param line: Исходная строка для преобразования шифром Цезаря
    :param password: Пароль (только буквы), которым осуществляется шифрование. Регистронезависим!
    :param offset: смещение для кодирования шифром Цезаря (0 - оставить без преобразования)
                   смещение может быть как положительным, так и отрицательным,
                   кроме того, смещение может быть больше чем количество символов
                   в алфавите (в данном случае корректное смещение будет вычислено
                   автоматически, причем отдельно для русского и английского алфавитов)
    :return: Измененная строка, полученная из исходной
    """
    assert(password.isalpha())
    password = password.lower()
    password_len = len(password)
    password_idx = 0

    result = ''

    for char in line:
        # Get password char
        if password_idx >= password_len:
            password_idx = 0
        pass_char = password[password_idx]
        if pass_char in eng_abc:
            pass_offset = eng_abc.find(pass_char)
        elif pass_char in rus_abc:
            pass_offset = rus_abc.find(pass_char)
        if neg_pass_offset == True:
            pass_offset = -pass_offset

        # Get char in line
        if (char in eng_abc) or (char in ENG_ABC):
            if char in eng_abc:
                current_abc = eng_abc
            else:
                current_abc = ENG_ABC
            abc_position = current_abc.find(char) + offset + pass_offset
            if abc_position >= len_eng_abc:
                abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
            if abc_position <= -len_eng_abc:
                abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
            char = str(current_abc[abc_position])
            password_idx += 1
        elif (char in rus_abc) or (char in RUS_ABC):
            if char in rus_abc:
                current_abc = rus_abc
            else:
                current_abc = RUS_ABC
            abc_position = current_abc.find(char) + offset + pass_offset
            if abc_position >= len_rus_abc:
                abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
            if abc_position <= -len_rus_abc:
                abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
            char = str(current_abc[abc_position])
            password_idx += 1
        result += char
    return result

def vigenere_dec(line, password, offset=0):
    """
    Дещифрация строки зашифрованной шифром Виженера
    :param line: исходная строка
    :param password: Пароль для дешифрации, которым была зашифрована строка
    :param offset: смещение для шифра Цезаря (то же самое, что было использовано при шифрации)
    :return: декодированная строка
    """
    return vigenere_enc(line, password, offset=-offset, neg_pass_offset=True)

# ====== РАБОТА С ФАЙЛАМИ =======
def vigenere_file_enc(filename, password, offset=0, neg_pass_offset=False):
    """
    Кодирование строки шифром Виженера
    (эта же функция применяется для дешифрации с обратным (отрицательным) смещением,
    т.е. если кодируем со смещением 10, то декодируем со смещением -10)
    :param line: Исходная строка для преобразования шифром Цезаря
    :param password: Пароль (только буквы), которым осуществляется шифрование. Регистронезависим!
    :param offset: смещение для кодирования шифром Цезаря (0 - оставить без преобразования)
                   смещение может быть как положительным, так и отрицательным,
                   кроме того, смещение может быть больше чем количество символов
                   в алфавите (в данном случае корректное смещение будет вычислено
                   автоматически, причем отдельно для русского и английского алфавитов)
    :return: Измененная строка, полученная из исходной
    """
    assert(password.isalpha())
    password = password.lower()
    password_len = len(password)
    password_idx = 0

    result = ''
    for line in open(filename):
        for char in line:
            # Get password char
            if password_idx >= password_len:
                password_idx = 0
            pass_char = password[password_idx]
            if pass_char in eng_abc:
                pass_offset = eng_abc.find(pass_char)
            elif pass_char in rus_abc:
                pass_offset = rus_abc.find(pass_char)
            if neg_pass_offset == True:
                pass_offset = -pass_offset

            # Get char in line
            if (char in eng_abc) or (char in ENG_ABC):
                if char in eng_abc:
                    current_abc = eng_abc
                else:
                    current_abc = ENG_ABC
                abc_position = current_abc.find(char) + offset + pass_offset
                if abc_position >= len_eng_abc:
                    abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
                if abc_position <= -len_eng_abc:
                    abc_position = abc_position - len_eng_abc * (abc_position // len_eng_abc)
                char = str(current_abc[abc_position])
                password_idx += 1
            elif (char in rus_abc) or (char in RUS_ABC):
                if char in rus_abc:
                    current_abc = rus_abc
                else:
                    current_abc = RUS_ABC
                abc_position = current_abc.find(char) + offset + pass_offset
                if abc_position >= len_rus_abc:
                    abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
                if abc_position <= -len_rus_abc:
                    abc_position = abc_position - len_rus_abc * (abc_position // len_rus_abc)
                char = str(current_abc[abc_position])
                password_idx += 1
            result += char
    return result

def vigenere_file_dec(filename, password, offset=0):
    """
    Дещифрация строки зашифрованной шифром Виженера
    :param line: исходная строка
    :param password: Пароль для дешифрации, которым была зашифрована строка
    :param offset: смещение для шифра Цезаря (то же самое, что было использовано при шифрации)
    :return: декодированная строка
    """
    return vigenere_file_enc(filename, password, offset=-offset, neg_pass_offset=True)


# Тесты
if __name__ == '__main__':
    st = 'Яртпцв, Дтэбфр т Ъощбх!'
    print(vigenere_dec(st, 'ПАЙНС'))
