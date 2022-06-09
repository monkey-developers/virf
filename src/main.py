from os import path
from PyQt5 import uic, QtWidgets

from tictactoe import game, logic

from hanggame import hanggame, hanggamelogic

def main():
    app = QtWidgets.QApplication([])
    execpath = path.dirname(__file__)
    ui = uic.loadUi(path.join(execpath, "screen.ui"))
    ui.show()

    # Fix button image problems
    ui.setStyleSheet(f'background-image : url(src/background.png);')
    ui.ticTacToe.setStyleSheet(f'background-image : url(src/tictactoe.jpg); border-radius: 8px;')
    ui.hangGame.setStyleSheet(f'background-image : url(src/hanggame.jpg); border-radius: 8px;')
    ui.joKenPo.setStyleSheet(f'background-image : url(src/jokenpo.png); border-radius: 8px;')
    ui.github.setStyleSheet(f'background-image : url(src/github.jpg); border-radius: 8px;')

    ui.ticTacToe.clicked.connect(game.play)
    ui.hangGame.clicked.connect(hanggame.play)

    app.exec()

if __name__ == "__main__":
    main()