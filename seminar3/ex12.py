from operator import indexOf


def group_by_rhyme(list):
    toReturnList = {}

    for word in list:
        key = word[len(word)-2:]
        if key not in toReturnList:
            toReturnList[key] = []
        toReturnList[key].append(word)
    return [*toReturnList.values()]


list = []

n = int(input("Enter number of words in list: "))

for i in range(0, n):
    el = input()
    list.append(el)

print(group_by_rhyme(list))
