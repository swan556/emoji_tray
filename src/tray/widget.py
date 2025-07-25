from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QMainWindow
from functools import partial
import csv

dataset = "./dataset/full_emoji.csv" # dataset location
emoji_list = list(csv.reader(open(dataset, "r")))[1:] # list of all emojis
num_emojis = len(emoji_list) # total number of emojis

n_col = 8
n_row = num_emojis//n_col

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 500)
        main_widget = QWidget()

        v_layout = QVBoxLayout(main_widget)

        for r in range(n_row):

            h_layout = QHBoxLayout()

            for c in range(n_col):

                emoji = emoji_list[r*n_col + c][1]
                emoji_btn = QPushButton(f"{emoji}")
                emoji_btn.setFixedSize(50, 50)
                emoji_btn.setStyleSheet("font-size: 37px;")
                emoji_btn.pressed.connect(partial(self.emoji_pressed, emoji))

                h_layout.addWidget(emoji_btn)
            
            v_layout.addLayout(h_layout)

        scroll = QScrollArea()
        scroll.setWidget(main_widget)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

    
    def emoji_pressed(self, emoji):
        print("pressed: ", emoji)