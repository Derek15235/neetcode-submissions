class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right > left:
            leftVal = s[left]
            rightVal = s[right]

            if not leftVal.isalnum():
                left += 1
                continue
            elif not rightVal.isalnum():
                right -= 1
                continue

            if leftVal.lower() != rightVal.lower():
                return False
            else:
                left += 1
                right -= 1
        return True