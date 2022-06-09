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
    ui.ticTacToe.setStyleSheet(f'background-image : url(src/tictactoe.jpg);')
    ui.hangGame.setStyleSheet(f'background-image : url(src/hanggame.jpg);')
    ui.joKenPo.setStyleSheet(f'background-image : url(src/jokenpo.jpg);')
    ui.github.setStyleSheet(f'background-image : url(src/github.jpg);')

    ui.ticTacToe.clicked.connect(game.play)
    ui.hangGame.clicked.connect(hanggame.play)

    app.exec()

if __name__ == "__main__":
    main()