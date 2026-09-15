class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        row=[]
        column=[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row.append(i)
                    column.append(j)
        for i in range(r):
            if i in row:
                for j in range(c):
                    matrix[i][j]=0
            else:
                for j in column:
                    matrix[i][j]=0
