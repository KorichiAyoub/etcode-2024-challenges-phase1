def is_valid(matrix):
    n = len(matrix)
    for row in matrix:
        if sorted(row) != list(range(1, n + 1)):
            return False
    for j in range(n):
        column = [matrix[i][j] for i in range(n)]
        if sorted(column) != list(range(1, n + 1)):
            return False
    
    return True

matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
print(is_valid(matrix))  
