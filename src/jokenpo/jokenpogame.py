from os import path
from random import randint
from time import sleep
from PyQt5 import uic, QtWidgets, QtGui
import threading


def play():

    app = QtWidgets.QApplication([])

    ui = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))
    ui.show()

    values = ["rock", "paper", "scissor"]

    def flash_scores(draw, humanWin):
        if draw: 
            ui.ScoreHuman.setStyleSheet("color: blue;")
            ui.ScoreRobot.setStyleSheet("color: blue;")
        else: 
            if humanWin: ui.ScoreHuman.setStyleSheet("color: green;")
            else: ui.ScoreRobot.setStyleSheet("color: red;")
        sleep(0.250)
        ui.ScoreHuman.setStyleSheet("color: black;")
        ui.ScoreRobot.setStyleSheet("color: black;")

    def win(isHuman, humanScore, robotScore):
        
        if isHuman: ui.ScoreResult.setText("you win"); humanScore +=1; ui.ScoreHuman.setText(str(humanScore))
        else: ui.ScoreResult.setText("you lose"); robotScore +=1; ui.ScoreRobot.setText(str(robotScore))

        if isHuman: threading.Thread(target=lambda:flash_scores(False, True)).start()
        else: threading.Thread(target=lambda:flash_scores(False, False)).start()

        ui.ScoreHuman.setText(str(humanScore))
        ui.ScoreRobot.setText(str(robotScore))

    def turn(humanSelected):
        robotSelected = values[randint(0,2)]
        
        humanScore, robotScore = int(ui.ScoreHuman.text()), int(ui.ScoreRobot.text())

        if (humanSelected == robotSelected):
            ui.ScoreResult.setText("draw")
            threading.Thread(target=lambda:flash_scores(True, False)).start()
            return
        if (humanSelected == "rock"):
            if robotSelected == "scissor": win(isHuman=True, humanScore=humanScore, robotScore=robotScore)
            else: win(isHuman=False, humanScore=humanScore, robotScore=robotScore)
        if (humanSelected == "paper"):
            if robotSelected == "rock": win(isHuman=True, humanScore=humanScore, robotScore=robotScore)
            else: win(isHuman=False, humanScore=humanScore, robotScore=robotScore)
        if (humanSelected == "scissor"):
            if robotSelected == "paper": win(isHuman=True, humanScore=humanScore, robotScore=robotScore)
            else: win(isHuman=False, humanScore=humanScore, robotScore=robotScore)


    ui.setStyleSheet('background-image : url(src/jokenpo/assets/background.png);')
    ui.setWindowIcon(QtGui.QIcon('src/jokenpo.png'))
    QtGui.QFontDatabase.addApplicationFont("src/arcade.ttf")

    ui.buttonRock.clicked.connect(lambda: turn(values[0]))
    ui.buttonPaper.clicked.connect(lambda: turn(values[1]))
    ui.buttonScissor.clicked.connect(lambda: turn(values[2]))

    app.exec()

if __name__ == "__main__":
    play()
    