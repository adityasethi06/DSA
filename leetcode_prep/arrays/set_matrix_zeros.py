# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        top_left = -1
        rows = len(matrix)
        cols = len(matrix[0])
        for i, el in enumerate(matrix):
            for j, _ in enumerate(el):
                if not matrix[i][j]:
                    if not i:
                        top_left = 0
                        continue
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for i in range(rows):
                matrix[i][0] = 0
        if not top_left:
            for c in range(cols):
                matrix[0][c] = 0

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

# 0,1,2,0
# 3,4,5,2
# 1,3,1,5

# 0,1,2,0
# 3,4,5,2
# 1,3,1,5