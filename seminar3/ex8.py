def findCharactersByUnicode(x=1, list=[], flag=True):
    toReturnList = []
    for word in list:
        if flag == True:
            toReturnList.append(
                [character for character in word if ord(character) % x == 0])
        else:
            toReturnList.append(
                [character for character in word if ord(character) % x != 0])

    return toReturnList


x = 2
flag = False
list = ["test", "hello", "lab002"]
print(findCharactersByUnicode(x, list, flag))
