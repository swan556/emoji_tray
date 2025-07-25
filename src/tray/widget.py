from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QMainWindow
from functools import partial
from PySide6.QtCore import Qt
import time
import csv, subprocess
from pynput import mouse
import pyautogui
import pyperclip

dataset = "/home/swan/Documents/py_files/emoji_tray_for_linux/dataset/full_emoji.csv" # dataset location
emoji_list = list(csv.reader(open(dataset, "r")))[1:] # list of all emojis
num_emojis = len(emoji_list) # total number of emojis

n_col = 8
n_row = num_emojis//n_col

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.Tool, True)
        self.setFocusPolicy(Qt.NoFocus)

        listener = mouse.Listener(on_click=self.on_click)
        listener.start()

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
        pyperclip.copy(emoji)
        current_position = pyautogui.position()
        if saved_position:
            pyautogui.click(saved_position)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.moveTo(current_position)
    def on_click(self, x, y, button, pressed):
        if pressed:
            global saved_position
            saved_position = (x, y)
            return False
