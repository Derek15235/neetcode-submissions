class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        def dfs(path):
            if len(used) == len(nums):
                res.append(path[:])
                return

            # Include
            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    dfs(path)
                    path.pop()
                    used.remove(num)
        dfs([])
        return res