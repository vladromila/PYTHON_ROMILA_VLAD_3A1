def operations(*sets):
    toReturnSet = {}
    for i in range(0, len(sets)):
        for j in range(i+1, len(sets)):
            toReturnSet["{} | {}".format(sets[i], sets[j])] = set(
                sets[i].union(sets[j]))
            toReturnSet["{} & {}".format(sets[i], sets[j])] = sets[i] & sets[j]
            toReturnSet["{} - {}".format(sets[i], sets[j])] = sets[i] - sets[j]
            toReturnSet["{} - {}".format(sets[j], sets[i])] = sets[j] - sets[i]

    return toReturnSet


print(operations({1, 2}, {2, 3}))
