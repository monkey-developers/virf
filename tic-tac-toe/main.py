from os import path
from PyQt5 import uic, QtWidgets

from game import *

def start_game(ui):
    ui.startButton.hide()
    setup(ui)

def main():
    app = QtWidgets.QApplication([])
    ui = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))

    ui.startButton.clicked.connect(lambda: start_game(ui))
    # start_game(ui)

    ui.show()
    app.exec()

if __name__ == "__main__":
    main()