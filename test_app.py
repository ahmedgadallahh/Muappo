import pytest
from main import TicTacToeApp


def test_app_initialization():
    """يتأكد إن التطبيق بيتبني من غير أخطاء"""
    app = TicTacToeApp()
    assert app is not None
    assert isinstance(app.players, list)
    assert app.scores == {"X": 0, "O": 0}
