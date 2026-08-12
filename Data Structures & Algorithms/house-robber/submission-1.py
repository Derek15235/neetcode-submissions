class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        D = [0] * len(nums)
        
        D[0] = nums[0]
        D[1] = max(nums[0], nums[1])
        for i in range (2, len(nums)):
            D[i] = max(D[i-1], nums[i] + D[i - 2])
        return D[len(nums) - 1]