def findOccurrences(list, x):
    toReturnList = []
    newList = []
    for sublist in list:
        newList = [*newList, *sublist]
    uniqueElements = set(newList)
    for el in uniqueElements:
        if newList.count(el) == 2:
            toReturnList.append(el)
    return toReturnList


list = [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]

print(findOccurrences(list, 2))
