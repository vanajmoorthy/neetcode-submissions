class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = board
        cols = list(zip(*board))

        for row in rows:
            if not self.isValidRowOrCol(row):
                return False

        for col in cols:
            if not self.isValidRowOrCol(col):
                return False


        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                # (r, c) is top-left corner of each box
                box = [board[i][j] for i in range(r, r+3) for j in range(c, c+3)]
                if not self.isValidRowOrCol(box):
                    return False
        
        return True

    def isValidRowOrCol(self, row) -> bool:
        visited = {}

        for item in row:
            if item in visited:
                visited[item] += 1
            else:
                visited[item] = 1
        
        for key, val in visited.items():
            if key != "." and val > 1:
                return False
        return True

    