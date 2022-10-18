def replaceElementsUnderDiagonal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and j < i:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5],
          [5, 5, 2, 5, 6, 4],
          [1, 2, 3, 2, 1, 1],
          ]
for el in replaceElementsUnderDiagonal(matrix):
    print(el)
