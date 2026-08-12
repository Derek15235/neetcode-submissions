class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket each number by frequency (0 - n buckets)
        freq_buckets = [[] for i in range(len(nums) + 1)]
        # Get frequencies
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        for key in counts:
            freq_buckets[counts[key]].append(key)

        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for val in freq_buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res