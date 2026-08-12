class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        starts = set()

        # get all the numbers that would start the sequence
        for num in setNums:
            if num - 1 not in starts:
                starts.add(num)
        
        # Find all sequences and save longest based off of length
        bestSeq = 0
        for start in starts:
            currSeq = 1
            currNum = start
            while currNum + 1 in setNums:
                currSeq += 1
                currNum += 1
            bestSeq = max(bestSeq, currSeq)

        return bestSeq

        