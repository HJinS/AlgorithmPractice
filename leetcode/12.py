class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        roman_unit = list(roman.keys())
        idx = 0
        while idx < len(roman_unit) and num >= roman_unit[idx]:
            idx += 1
                
        idx -= 1
        res = ""
        while idx >= 0:
            unit = roman_unit[idx]
            n = num // unit
            remain = num % unit
            if n == 0:
                idx -= 1
                continue
            for i in range(n):
               res += roman[unit] 
            num %= unit
            idx -= 1
                
        return res