

def to_roman_conv(arabic_number):
    roman_list = ["C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    arab_list = [100, 90, 50, 40, 10, 9, 5, 4, 1]

    convert = ""
    n = 0
    while arabic_number > 0:

        for _ in range(arabic_number // arab_list[n]):
            convert += roman_list[n]
            arabic_number -= arab_list[n]
        n += 1
    return convert

