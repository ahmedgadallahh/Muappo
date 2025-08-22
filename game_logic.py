class TicTacToeLogic:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turn = 0
        self.scores = {"X": 0, "O": 0}

    def check_win(self, player):
        # الصفوف
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # الأعمدة
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # الأقطار
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def restart_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = 0
