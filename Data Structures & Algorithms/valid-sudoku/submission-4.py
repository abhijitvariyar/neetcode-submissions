class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, group = {}, {}, {}
        group_id = (1, 1)
        for x in range(9):
            curr_row = set()
            row[x] = curr_row
            for y in range(9):
                group_id = ((x)//3, (y)//3)
                curr_group = group.get(group_id, set())
                group[group_id] = curr_group
                cell_val = board[x][y]
                if not cell_val.isdecimal():
                    continue
                curr_col = col.get(y, set())
                col[y] = curr_col
                if cell_val in curr_col or cell_val in curr_row or cell_val in curr_group:
                    return False
                else:
                    row[x].add(cell_val)
                    col[y].add(cell_val)
                    group[group_id].add(cell_val)

        return True
