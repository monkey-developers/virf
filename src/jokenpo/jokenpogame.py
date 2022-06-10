from os import path
from random import randint
from PyQt5 import uic, QtWidgets, QtGui



def play():

    app = QtWidgets.QApplication([])

    ui = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))
    ui.show()

    values = ["rock", "paper", "scissor"]


    def win(isHuman, humanScore, robotScore):
        
        if isHuman: ui.ScoreResult.setText("you win"); humanScore +=1; ui.ScoreHuman.setText(str(humanScore))
        else: ui.ScoreResult.setText("you lose"); robotScore +=1; ui.ScoreRobot.setText(str(robotScore))

        ui.ScoreHuman.setText(str(humanScore))
        ui.ScoreRobot.setText(str(robotScore))

    def turn(humanSelected):
        robotSelected = values[randint(0,2)]

        humanScore, robotScore = int(ui.ScoreHuman.text()), int(ui.ScoreRobot.text())

        if (humanSelected == robotSelected):
            ui.ScoreResult.setText("draw")
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
    QtGui.QFontDatabase.addApplicationFont("src/arcade.ttf")

    ui.buttonRock.clicked.connect(lambda: turn(values[0]))
    ui.buttonPaper.clicked.connect(lambda: turn(values[1]))
    ui.buttonScissor.clicked.connect(lambda: turn(values[2]))

    app.exec()

if __name__ == "__main__":
    play()
    