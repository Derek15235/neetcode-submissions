class Solution:
    def isPalindrome(self, s: str) -> bool:
        point_one = 0
        point_two = len(s) - 1

        while point_one < point_two:
            if s[point_one].lower() != s[point_two].lower():
                if not s[point_one].isalnum():
                    point_one += 1
                elif not s[point_two].isalnum():
                    point_two -= 1
                else:
                    return False
            else:
                point_one += 1
                point_two -= 1
        return True
        