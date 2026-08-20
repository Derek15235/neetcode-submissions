import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        res = [-heap[0][0]]
        # r is right most element in window
        for r in range(k, len(nums)):
            # l is left most element in window
            l = r - k + 1
            # Kick out invalid max's first
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            
            heapq.heappush(heap, (-nums[r], r))
            res.append(-heap[0][0])
        return res



