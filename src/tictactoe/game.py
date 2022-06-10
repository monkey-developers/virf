from os import path
from PyQt5 import uic, QtWidgets, QtGui

from tictactoe.logic import *

from tictactoe.assets import resources

def start_game(ui):
    ui.startButton.hide()
    ui.resetButton.hide()
    setup(ui)

def play():
    print("playing tictactoe")
    
    ui = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))

    QtGui.QFontDatabase.addApplicationFont("src/Minecraft.ttf")
    QtGui.QFontDatabase.addApplicationFont("src/arcade.ttf")

    ui.setStyleSheet(f'background-image : url(src/tictactoe/assets/background.png);')
    ui.label.setAutoFillBackground(True);
    ui.label.setStyleSheet("QLabel { background: transparent; color : #011E31; }")
    ui.label.setText("Bem vindo!")
    for i in range(9): 
        eval('ui.button{}.setStyleSheet("background-image : url(src/tictactoe/assets/obsidian-block.png); color: white;")'.format(i))
    ui.startButton.clicked.connect(lambda: start_game(ui))
    ui.resetButton.hide()

    ui.show()
    