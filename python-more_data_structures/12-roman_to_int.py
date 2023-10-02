#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string)
    roman_list.reverse()
    sum = 0
    for i in range(len(roman_list)):
        if i > 0 and roman_dict[roman_list[i]] < roman_dict[roman_list[i - 1]]:
            sum -= roman_dict[roman_list[i]]
        else:
            sum += roman_dict[roman_list[i]]
    return sum
