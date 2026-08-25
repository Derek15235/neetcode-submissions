class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, curTotal, path):
            if curTotal == target:
                res.append(path[:])
                return
            if start == len(candidates) or curTotal > target:
                return
            
            path.append(candidates[start])
            dfs(start+1, curTotal + candidates[start], path)
            path.pop()
            
            while start + 1 < len(candidates) and candidates[start] == candidates[start+1]:
                start += 1
            
            dfs(start+1, curTotal, path)
                
        dfs(0, 0, [])
        return res