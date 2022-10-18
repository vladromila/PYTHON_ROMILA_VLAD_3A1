def findPeople(matrix):
    toReturnPositions = []
    for i in range(0, len(matrix[0])):
        for j in range(len(matrix)-1, -1, -1):
            for k in range(j-1, -1, -1):
                print(i, j, k)
                if j != k:
                    if (matrix[j][i] <= matrix[k][i]):
                        if (i, j) not in toReturnPositions:
                            toReturnPositions.append((j, i))
    return toReturnPositions


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

print(findPeople(matrix))
