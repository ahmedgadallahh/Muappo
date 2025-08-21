from kivy.lang import builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

class TicTacToeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turn = 0
        self.scores = {"X": 0, "O": 0}

    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(None, None), size=(300, 400))
        layout.bind(pos=self.update_background)

        self.board_label = MDLabel(text="Tic Tac Toe", halign="center", theme_text_color="Custom", text_color=(1, 0, 2, 1))
        layout.add_widget(self.board_label)

        restart_button = MDRaisedButton(text="Restart", on_press=self.restart_game, md_bg_color=(0, 2, 0, 2))
        layout.add_widget(restart_button)  # Set md_bg_color to green (R=0, G=1, B=0)

        self.score_label = MDLabel(text=f"X Score: {self.scores['X']} | O Score: {self.scores['O']}", halign="center")
        layout.add_widget(self.score_label)

        for i in range(3):
            row_layout = MDBoxLayout(orientation='horizontal')
            for j in range(3):
                button = MDRaisedButton(text=" ", on_press=lambda x, row=i, col=j: self.on_button_press(row, col))
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, row, col):
        player = self.players[self.turn % 2]

        if self.board[row][col] == " ":
            self.board[row][col] = player
            self.update_board_label()

            if self.check_win(player):
                self.board_label.text = f"Player {player} wins!"
                self.scores[player] += 1
                self.score_label.text = f"X Score: {self.scores['X']} | O Score: {self.scores['O']}"
         
            elif self.is_board_full():
                self.board_label.text = "It's a draw!"
            else:
                self.turn += 1

    def update_board_label(self):
        board_str = ""
        for row in self.board:
            board_str += " | ".join(row) + "\n"
            board_str += "-" * 5 + "\n"
        self.board_label.text = board_str

    def check_win(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def restart_game(self, instance):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = 0
        self.update_board_label()
        self.board_label.text = "Tic Tac Toe"

    def update_background(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=instance.pos, size=instance.size) 

if __name__ == "__main__":
    TicTacToeApp().run()