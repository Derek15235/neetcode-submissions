class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        numList = []
        def dfs(start, path):
            if start == len(nums):
                numList.append(path[:])
                return

            path.append(nums[start])
            dfs(start+1, path)
            path.pop()
            dfs(start+1, path)
        dfs(0, [])
        return numList
            

        