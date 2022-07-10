def parse_int(string):
    str_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
        'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000
    }
    unit_group = ['hundred', 'thousand', 'million', 'billion']
    res = 0
    num = 0
    tmp = 0
    string = list(string.split(' '))
    for word in string:
        if word == 'and':
            continue
        if word not in unit_group:
            if '-' not in word:
                num += str_to_int[word]
            else:
                words = word.split('-')
                for item in words:
                    num += str_to_int[item]
        else:
            if word == 'hundred':
                tmp = num * str_to_int[word]
                num = 0
            else:
                if tmp:
                    num += tmp
                    res += num * str_to_int[word]
                    tmp = 0
                    num = 0
                else:
                    res += num * str_to_int[word]
                    num = 0
    res += num
    res += tmp
    return res

