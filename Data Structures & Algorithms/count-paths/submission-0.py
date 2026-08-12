class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numPaths = [[0 for _ in range(n)] for _ in range(m)]
        numPaths[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row != 0:
                    numPaths[row][col] += numPaths[row-1][col]
                if row != m-1:
                    numPaths[row][col] += numPaths[row+1][col]
                if col != 0:
                    numPaths[row][col] += numPaths[row][col-1]
                if col != n-1:
                    numPaths[row][col] += numPaths[row][col+1]
        return numPaths[m-1][n-1]