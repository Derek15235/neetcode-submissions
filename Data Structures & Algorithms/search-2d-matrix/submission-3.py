class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row that the target would exist in if at all
        l, r = 0, len(matrix) - 1
        midRow = 0
        while l <= r:
            midRow = (l+r) // 2
            if matrix[midRow][0] == target:
                return True
            elif matrix[midRow][0] < target:
                l = midRow + 1
            else:
                r = midRow - 1
        
        # After binary search, if target wasn't found at index 0, 
        # 'r' points to the potential row containing the target
        row = r
        if row < 0:
            return False

        # Regular binary search for target in selected row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            

