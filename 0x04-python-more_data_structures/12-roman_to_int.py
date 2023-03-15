#!/usr/bin/python3


def placeholder(place={}, string=''):
    num = 0
    temp_num = 0
    temp_key = ''
    for k, v, in place.items():
        if string.find(k) >= 0:
            temp_num = v
            temp_key = k
            continue
    num += temp_num
    new_str = string.replace(temp_key, '')
    return num, new_str


def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    roman = roman_string.upper()
    unit = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6,
            'VII': 7, 'VIII': 8, 'IX': 9}
    tens = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60,
            'LXX': 70, 'LXXX': 80, 'XC': 90}
    hundreds = {'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
                'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
    thousands = {'M': 1000, 'MM': 2000, 'MMM': 3000}

    total = 0
    num, new_roman = placeholder(unit, roman)
    total += num
    num, new_roman = placeholder(tens, new_roman)
    total += num
    num, new_roman = placeholder(hundreds, new_roman)
    total += num
    num, new_roman = placeholder(thousands, new_roman)
    total += num

    return total
