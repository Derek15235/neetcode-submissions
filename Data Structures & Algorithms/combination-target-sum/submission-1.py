class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, curTotal, path):
            if curTotal == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if curTotal + num <= target:                    
                    path.append(num)
                    dfs(i, curTotal + num, path)
                    path.pop()
        dfs(0, 0, [])
        return res