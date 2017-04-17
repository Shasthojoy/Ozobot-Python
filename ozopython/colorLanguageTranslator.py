class ColorLanguageTranslator:
    START = "CRYCYMCRW"
    END = "CMW"

    @staticmethod
    def base7(num):
        numerals = "0123456"
        return ((num == 0) and numerals[0]) or (ColorLanguageTranslator.base7(num // 7).lstrip(numerals[0]) + numerals[num % 7])

    # Function for converting a base-7 number(given as a string) to a 3 digit color code:
    @staticmethod
    def base7_to_color_code(num):
        colorDict = {
            '0': 'K',
            '1': 'R',
            '2': 'G',
            '3': 'Y',
            '4': 'B',
            '5': 'M',
            '6': 'C',
        }

        if len(num) == 1:
            num = "00" + num
        elif len(num) == 2:
            num = "0" + num

        chars = list(num)

        return colorDict[chars[0]] + colorDict[chars[1]] + colorDict[chars[2]]

    @staticmethod
    def translate(byte_array):
        color_sequence = "".join([ColorLanguageTranslator.base7_to_color_code(ColorLanguageTranslator.base7(int(str(x)))) for x in byte_array])

        sequence_with_repetition = ColorLanguageTranslator.START + color_sequence + ColorLanguageTranslator.END

        end_sequence = ""
        for i, c in enumerate(sequence_with_repetition):
            if i == 0 or sequence_with_repetition[i - 1] != c or end_sequence[i - 1] == 'W':
                end_sequence += c
            else:
                end_sequence += 'W'

        return end_sequence