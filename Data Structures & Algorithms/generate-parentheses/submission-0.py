class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(start, openCounts, closedCounts, path):
            if start == 2 * n:
                res.append("".join(path))
                return

            if openCounts < n:
                path.append('(')
                dfs(start + 1, openCounts +1, closedCounts, path)
                path.pop()
            
            if closedCounts < openCounts:
                path.append(')')
                dfs(start + 1, openCounts, closedCounts + 1, path)
                path.pop()
            
        dfs(0, 0, 0, [])
        return res