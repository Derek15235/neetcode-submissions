class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Indexed array, 0: a, 1:b .... 25:z
        first = [0] * 26
        for c in s1:
            first[ord(c) - ord('a')] += 1

        l, r = 0, len(s1) - 1
        # Loop through each substring in s2 with the lenght of s1
        while r < len(s2):
            second = [0] * 26
            for i in range(len(s1)):
                c = s2[l + i]
                second[ord(c) - ord('a')] += 1
            if first == second:
                return True
            else:
                l += 1
                r += 1
        return False


        # # Loop through each string and get character counts
        # for i in range(len(s1)):
        #     first[ord(s1[i]) - ord('a')] += 1
        # for i in range(len(s2)):
        #     second[ord(s2[i]) - ord('a')] += 1
        # print(first)
        # print(second)
        # # For each letter count, the second should have a minimum of the first count
        # for i in range(len(first)):
        #     if first[i] > second[i]:
        #         return False

        # return True


        


        