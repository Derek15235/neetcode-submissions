class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        prefix, suffix = [0] * len(height), [0] * len(height)

        # Prefix
        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        
        # Suffix
        suffix[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]
        return res
        
        

            
        
        


        