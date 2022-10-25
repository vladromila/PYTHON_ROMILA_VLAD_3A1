def listDup(l):
    uniqueElements = set(l)
    for el in uniqueElements:
        for i in range(0, len(l)):
            if el == l[i]:
                l.remove(el)
                break
    return (len(set(uniqueElements-set(l))), len(set(l)))


print(listDup([1, 1, 1, 3, 4, 5, 2, 2, 3, 6, 7, 8]))
