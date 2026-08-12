from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        '''
        Bucket Solution
        Have an array where the index is the count and the value is a list of numbers
        from nums that have that count.
        Once the numbers are put into their respective buckets, go backwards, appending
        every value in each bucket (iterate buckets left to right for decreasing order).
        Once the list has length k, return it.
        '''
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        

        
