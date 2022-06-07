class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
        roman = ""
        while num > 0:
            if 900 <= num < 1000:
                num -= 900
                roman += "CM"
            elif 400 <= num < 500:
                num -= 400
                roman += "CD"
            elif 90 <= num < 100:
                num -= 90
                roman += "XC"
            elif 40 <= num < 50:
                num -= 40
                roman += "XL"
            elif num == 9:
                num -= 9
                roman += "IX"
            elif num == 4:
                num -= 4
                roman += "IV"
            else:
                for i in symbol.keys():
                    if num // i > 0:
                        roman += (symbol[i] * (num // i))
                        num %= i
                        break
        return roman