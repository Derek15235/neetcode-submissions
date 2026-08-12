class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create prefix and suffix product lists, index is the excluded
        pre_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            if i == 1:
                pre_prod[i] = nums[0]
            else:
                pre_prod[i] = pre_prod[i-1] * nums[i - 1]
        
        suf_prod = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                suf_prod[i] = nums[i + 1]
            else:
                suf_prod[i] = suf_prod[i+1] * nums[i + 1]
        print(suf_prod)
        
        res = []
        for i in range(len(nums)):
            res.append(pre_prod[i] * suf_prod[i])
        return res