class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            box_dict = {}
            for j in range(0,9):
                if board[i][j] in box_dict and board[i][j] != ".":
                    return False
                box_dict[board[i][j]] = 0
        for i in range(0,9):
            box_dict = {}
            for j in range(0,9):
                if board[j][i] in box_dict and board[j][i] != ".":
                    return False
                box_dict[board[j][i]] = 0
        
        for vert in range (3):
            for hor in range(3):
                box_dict = {}
                for i in range(vert*3,vert*3+3):
                    for j in range(hor*3,hor*3+3):
                        if board[i][j] in box_dict and board[i][j] != '.':
                            return False
                        box_dict[board[i][j]] = 0
        return True



        return True