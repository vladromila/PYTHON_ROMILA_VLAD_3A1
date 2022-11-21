import re


def cenzurare(text):
    toReturnText = ""
    for word in text.split(" "):
        if re.match(r"^[aeiou].*[aeiou]$", word) != None:
            k = 0
            for l in word:
                if k % 2 == 0:
                    toReturnText += l
                else:
                    toReturnText += "*"
                k += 1
        else:
            toReturnText += word
        toReturnText += " "
    return toReturnText


print(cenzurare("abcde"))
