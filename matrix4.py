def checkio(matrix):
    #replace this for solution
    line = 1
    column = 1
    diag = 1
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix[j])):
            if matrix[i][j] == matrix[(i+1)%len(matrix)][j] and (i+1)%len(matrix) != 0:
                column += 1
            else:
                column = 1
            if line >= 4 or column >= 4 or diag >= 4:
                return True
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == matrix[i][(j+1)%len(matrix[i])] and (j+1)%len(matrix[i]) != 0:
                line += 1
            else:
                line = 1
            if line >= 4 or column >= 4 or diag >= 4:
                return True
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i+1 < len(matrix) and j+1 < len(matrix[0]) and i-1 >= 0 and j-1 >= 0:
                if matrix[i][j] == matrix[(i+1)][(j+1)]:
                    print(i, j, (i+1)%len(matrix), (j+1)%len(matrix[i]))
                    diag += 1
                elif matrix[i][j] == matrix[(i-1)][(j-1)]:
                    diag += 1
                else:
                    diag = 1
                print("i: ", i, " j: ", j, " valor: ", matrix[i][j], " diag: ", diag)
                if line >= 4 or column >= 4 or diag >= 4:
                    return True
            
    return False
