class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keys are values
        # Values are the index of the value (key)
        val_indexes = {}

        for i in range(len(nums)):
            if target - nums[i] in val_indexes:
                return [val_indexes[target - nums[i]], i]
            val_indexes[nums[i]] = i
        

        