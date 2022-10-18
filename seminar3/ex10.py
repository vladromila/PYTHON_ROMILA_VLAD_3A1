def generateTuples(list):
    toGenerateTuples = []
    for i in range(len(list[0])):
        toGenerateTuples.append(())
        for j in range(len(list)):
            toGenerateTuples[i] = (*toGenerateTuples[i], list[j][i])
            # toGenerateTuples[i] += (list[j][i],)
    return toGenerateTuples


list = [[1, 2, 3], [5, 6, 7], ["a", "b", "c"]]

print(generateTuples(list))
