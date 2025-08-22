from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Rectangle
from game_logic import TicTacToeLogic   # ✅ نستورد المنطق


class TicTacToeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logic = TicTacToeLogic()

    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20,
                             size_hint=(None, None), size=(300, 400))
        layout.bind(pos=self.update_background)

        self.board_label = MDLabel(text="Tic Tac Toe", halign="center",
                                   theme_text_color="Custom", text_color=(1, 0, 2, 1))
        layout.add_widget(self.board_label)

        restart_button = MDRaisedButton(
            text="Restart",
            on_press=self.restart_game,
            md_bg_color=(0, 2, 0, 2)
        )
        layout.add_widget(restart_button)

        self.score_label = MDLabel(
            text=f"X Score: {self.logic.scores['X']} | O Score: {self.logic.scores['O']}",
            halign="center"
        )
        layout.add_widget(self.score_label)

        for i in range(3):
            row_layout = MDBoxLayout(orientation='horizontal')
            for j in range(3):
                button = MDRaisedButton(
                    text=" ",
                    on_press=lambda x, row=i, col=j: self.on_button_press(row, col)
                )
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, row, col):
        player = self.logic.players[self.logic.turn % 2]

        if self.logic.board[row][col] == " ":
            self.logic.board[row][col] = player
            self.update_board_label()

            if self.logic.check_win(player):
                self.board_label.text = f"Player {player} wins!"
                self.logic.scores[player] += 1
                self.score_label.text = f"X Score: {self.logic.scores['X']} | O Score: {self.logic.scores['O']}"

            elif self.logic.is_board_full():
                self.board_label.text = "It's a draw!"
            else:
                self.logic.turn += 1

    def update_board_label(self):
        board_str = ""
        for row in self.logic.board:
            board_str += " | ".join(row) + "\n"
            board_str += "-" * 5 + "\n"
        self.board_label.text = board_str

    def restart_game(self, instance):
        self.logic.restart_game()
        self.update_board_label()
        self.board_label.text = "Tic Tac Toe"

    def update_background(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)   # أبيض للخلفية
            Rectangle(pos=instance.pos, size=instance.size)


if __name__ == "__main__":
    TicTacToeApp().run()
