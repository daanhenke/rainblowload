password_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z",
                       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z",
                       "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                       " ", "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<",
                       "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
                       ]


def encode(number, base=95):
    result = ""

    if number == 0:
        return "a"

    while number > 0:
        res = number / base
        rem = number % base
        result = password_characters[rem] + result
        number = res

    return result


def decode(string, base=95):
    number = 0
    length = len(string) - 1

    for item in string:
        part = password_characters.index(item)
        number += part * (base ** length)
        length -= 1

    return number
