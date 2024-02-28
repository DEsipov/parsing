""""
Основные методы модуля re.
"""

import re


def main():
    pattern = r'\d\d\.\d\d\.\d{4}'
    replace_str = 'DD.MM.YYYY'
    res = re.sub(pattern, replace_str,
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')
    print(res)


def foo():
    pattern = r'\d\d\-\d\d'
    match = re.search(pattern, 'Телефон 123-12-12-12')
    res = match and match[0]
    print(res)
    # -> 23-12
    # 12-12 не попадет в найденное, потому что попадает
    # только первое вхождение.
    print('*' * 30)

    # А так будет два матча найдены.
    match = re.findall(r'\d\d\D\d\d', r'Телефон 123-12883-12')
    print(match[0] if match else 'Not found')
    print(match[1] if match else 'Not found')

    match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
    print(match[0] if match else 'Not found')
    # -> Not found

    match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
    print('YES' if match else 'NO')
    # -> YES

    match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
    print('YES' if match else 'NO')
    # -> NO

    print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
    # -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']

    print(re.findall(r'\d\d\.\d\d\.\d{4}',
                     r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
    # -> ['19.01.2018', '01.09.2017']


    iterator = re.finditer(
            r'\d\d\.\d\d\.\d{4}',
            r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')
    for m in iterator:
        print('Дата', m[0], 'начинается с позиции', m.start())
    # -> Дата 19.01.2018 начинается с позиции 20
    # -> Дата 01.09.2017 начинается с позиции 45

    print(re.sub(r'\d\d\.\d\d\.\d{4}',
                 r'DD.MM.YYYY',
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
    # -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY


if __name__ == '__main__':
    main()