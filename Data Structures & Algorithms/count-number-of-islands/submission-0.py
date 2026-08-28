class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def getNeighbors(r, c):
            deltaRow = [1, 0, -1, 0]
            deltaCol = [0, 1, 0, -1]
            res = []
            for i in range(len(deltaRow)):
                rNew = r + deltaRow[i]
                cNew = c + deltaCol[i]
                if (rNew, cNew) in visited:
                    continue
                if 0 <= cNew < len(grid[0]) and 0 <= rNew < len(grid) and grid[r][c] == "1":
                    res.append((rNew, cNew))
            return res
        def dfs(r, c):
            visited.add((r,c))
            neighbors = getNeighbors(r,c)
            for rNew, cNew in neighbors:
                dfs(rNew, cNew)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count