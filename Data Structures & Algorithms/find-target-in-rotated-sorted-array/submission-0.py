class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        minRotate = 0
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= nums[-1]:
                minRotate = mid
                r = mid - 1
            else:
                l = mid + 1

        # Start from this index of the min 
        l, r = minRotate, minRotate + len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            midIndex = mid % len(nums)
            if nums[midIndex] == target:
                return midIndex
            elif nums[midIndex] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
             