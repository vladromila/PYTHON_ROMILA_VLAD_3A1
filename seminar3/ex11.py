def orderByTuples(list):

    swapped = False
    n = len(list)
    for i in range(n-1):

        for j in range(0, n-i-1):

            if list[j][1][2] > list[j + 1][1][2]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]

        if not swapped:
            break
    return list


list = [('abc', 'bcd'), ('abc', 'zza'), ('bbb', 'bbb')]
print(orderByTuples(list))
