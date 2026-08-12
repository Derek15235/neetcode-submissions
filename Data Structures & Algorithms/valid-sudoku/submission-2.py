class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                box_cord_row = int(row / 3)
                box_cord_col = int(col / 3)
                
                if val in rows[row] or val in cols[col] or val in boxes[(box_cord_row, box_cord_col)]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[(box_cord_row, box_cord_col)].add(val)
        return True