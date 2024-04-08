def int_to_roman(num):
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_number = ""
    for i in range(len(values)):
        while num >= values[i]:
            roman_number += symbols[i]
            num -= values[i]
    return roman_number


num = 4
print(int_to_roman(num))
