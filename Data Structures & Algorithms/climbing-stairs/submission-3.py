
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[0] = 1
        return self.climbStairsHelper(n, memo)

    def climbStairsHelper(self, n, memo):
        # Take one step or two steps and add their paths
        if n in memo:
            return memo[n]

        memo[n] = self.climbStairsHelper(n-1, memo) + self.climbStairsHelper(n-2, memo)
        return memo[n]