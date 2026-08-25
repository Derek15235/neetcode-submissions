class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, path):
            if start == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[start])
            dfs(start+1, path)
            path.pop()
            
            while start + 1 < len(nums) and nums[start] == nums[start+1]:
                start += 1
            
            dfs(start+1, path)
                
        dfs(0, [])
        return res
        