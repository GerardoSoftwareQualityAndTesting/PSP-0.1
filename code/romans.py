romans_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
               90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


def translate_num(num: int) -> str:
    ans = ""

    for roman in romans_dict:
        div = num // roman
        num %= roman
        while div:
            ans += romans_dict[roman]
            div -= 1

    return ans
