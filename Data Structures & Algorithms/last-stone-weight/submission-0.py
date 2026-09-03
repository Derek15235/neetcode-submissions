class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            firstBiggest = -1 * heapq.heappop(maxHeap)
            secondBiggest = -1 * heapq.heappop(maxHeap)

            if firstBiggest > secondBiggest:
                diff = -(firstBiggest - secondBiggest)
                heapq.heappush(maxHeap, diff)
        if len(maxHeap) == 1:
            return -maxHeap[0]
        return 0
        
                

