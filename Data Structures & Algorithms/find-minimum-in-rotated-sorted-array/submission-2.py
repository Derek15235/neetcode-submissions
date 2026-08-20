class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Find first true
        # Pivot: index where it is less than the first number
        l, r = 0, len(nums) - 1
        minRotate = r
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < nums[-1]:
                minRotate = mid
                r = mid - 1
            elif nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

        # Default: The array was rotated 360, aka len(nums)
        return nums[minRotate]