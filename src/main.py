from os import path
from PyQt5 import uic, QtWidgets, QtGui

from tictactoe import game, logic
from hanggame import hanggame, hanggamelogic
from jokenpo import jokenpogame
from webbrowser import open

def main():
    app = QtWidgets.QApplication([])
    execpath = path.dirname(__file__)
    ui = uic.loadUi(path.join(execpath, "screen.ui"))
    
    # Fix button image problems
    ui.setStyleSheet('background-image : url(src/background.png);')
    ui.setWindowIcon(QtGui.QIcon('src/virf.png'))
    ui.ticTacToe.setStyleSheet('background-image : url(src/tictactoe.jpg); border-radius: 8px;')
    ui.hangGame.setStyleSheet('background-image : url(src/hanggame.jpg); border-radius: 8px;')
    ui.joKenPo.setStyleSheet('background-image : url(src/jokenpo.png); border-radius: 8px;')
    ui.github.setStyleSheet('background-image : url(src/github.jpg); border-radius: 8px;')

    ui.joKenPo.clicked.connect(jokenpogame.play)
    ui.ticTacToe.clicked.connect(game.play)
    ui.hangGame.clicked.connect(hanggame.play)
    ui.github.clicked.connect(lambda: open("https://github.com/abehidek", new=2))
    
    ui.show()
    app.exec()

if __name__ == "__main__":
    main()