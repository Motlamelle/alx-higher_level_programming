#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    strng = list(roman_string[::-1].upper())
    flag = 1
    sum = 0
    for i in range(len(strng) - 1):
        sum = sum + numerals[strng[i]]*flag
        if numerals[strng[i]] <= numerals[strng[i + 1]]:
            flag = 1
        if numerals[strng[i]] > numerals[strng[i + 1]]:
            flag = -1
    if flag == 1:
        sum = sum + numerals[strng[len(strng) - 1]]
    if flag == -1:
        sum = sum - numerals[strng[len(strng) - 1]]
    return sum
