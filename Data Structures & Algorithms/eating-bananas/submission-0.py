import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Lower bound = 1
        # Upper bound = max of piles
        l, r = 1, max(piles)
        bestK = r
        while l <= r:
            k = (l+r) // 2
            # Can you eat all bannanas?
            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            # If so, update best value and bound it 
            if totalTime <= h:
                bestK = k
                r = k - 1
            # Else must be higher 
            else:
                l = k + 1
        return bestK

            

