class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}

        for i in range(len(nums)):
            if nums[i] in subs:
                return [subs[nums[i]], i]
            subs[target - nums[i]] = i
        

        