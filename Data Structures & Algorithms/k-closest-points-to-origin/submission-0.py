from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x1, y1 = point[0], point[1]
            dist = sqrt(x1*x1 + y1*y1)

            heapq.heappush(minHeap, (dist, x1, y1))
        res = []
        for i in range(k):
            point = heapq.heappop(minHeap)
            x, y = point[1], point[2]
            res.append([x,y])
        
        return res
        