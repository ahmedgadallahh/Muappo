import os

# نضمن إن Kivy يشتغل في وضع headless (بدون نافذة)
os.environ.setdefault("KIVY_NO_ARGS", "1")
os.environ.setdefault("KIVY_WINDOW", "mock")
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

from main import TicTacToeApp


def _make_app_without_kivy():
    """
    ننشئ كائن من غير استدعاء __init__ بتاع MDApp
    ونهيّأ المتغيرات الأساسية يدويًا.
    """
    app = TicTacToeApp.__new__(TicTacToeApp)
    app.board = [[" " for _ in range(3)] for _ in range(3)]
    app.players = ["X", "O"]
    app.turn = 0
    app.scores = {"X": 0, "O": 0}
    return app


def test_check_win_row():
    app = _make_app_without_kivy()
    app.board[0] = ["X", "X", "X"]
    assert app.check_win("X")


def test_check_win_col():
    app = _make_app_without_kivy()
    for r in range(3):
        app.board[r][1] = "O"
    assert app.check_win("O")


def test_check_win_diag():
    app = _make_app_without_kivy()
    for i in range(3):
        app.board[i][i] = "X"
    assert app.check_win("X")


def test_board_not_full_initially():
    app = _make_app_without_kivy()
    assert not app.is_board_full()
