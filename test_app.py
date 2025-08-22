from game_logic import TicTacToeLogic


def test_check_win_row():
    game = TicTacToeLogic()
    game.board[0] = ["X", "X", "X"]
    assert game.check_win("X")


def test_check_win_col():
    game = TicTacToeLogic()
    for r in range(3):
        game.board[r][1] = "O"
    assert game.check_win("O")


def test_check_win_diag():
    game = TicTacToeLogic()
    for i in range(3):
        game.board[i][i] = "X"
    assert game.check_win("X")


def test_board_not_full_initially():
    game = TicTacToeLogic()
    assert not game.is_board_full()


def test_restart_game():
    game = TicTacToeLogic()
    game.board[0] = ["X", "X", "X"]
    game.restart_game()
    assert all(cell == " " for row in game.board for cell in row)
    assert game.turn == 0
