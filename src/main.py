from os import path
from PyQt5 import uic, QtWidgets

from tictactoe import game, logic
from hanggame import hanggame, hanggamelogic
from jokenpo import jokenpogame

def main():
    app = QtWidgets.QApplication([])
    execpath = path.dirname(__file__)
    ui = uic.loadUi(path.join(execpath, "screen.ui"))
    
    # Fix button image problems
    ui.setStyleSheet('background-image : url(src/background.png);')
    ui.ticTacToe.setStyleSheet('background-image : url(src/tictactoe.jpg); border-radius: 8px;')
    ui.hangGame.setStyleSheet('background-image : url(src/hanggame.jpg); border-radius: 8px;')
    ui.joKenPo.setStyleSheet('background-image : url(src/jokenpo.png); border-radius: 8px;')
    ui.github.setStyleSheet('background-image : url(src/github.jpg); border-radius: 8px;')

    ui.joKenPo.clicked.connect(jokenpogame.play)
    ui.ticTacToe.clicked.connect(game.play)
    ui.hangGame.clicked.connect(hanggame.play)
    
    ui.show()
    app.exec()

if __name__ == "__main__":
    main()