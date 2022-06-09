from os import path
from PyQt5 import uic, QtWidgets

from tictactoe.logic import *

from tictactoe.assets import resources

def start_game(ui):
    ui.startButton.hide()
    ui.resetButton.hide()
    setup(ui)

def play():
    print("playing tictactoe")
    
    ui = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))
    ui.startButton.clicked.connect(lambda: start_game(ui))
    ui.resetButton.hide()

    ui.show()
    