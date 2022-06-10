from os import system, path
from PyQt5 import uic, QtWidgets, QtGui
import sys
from hanggame.hanggamelogic import *

def play():
    def setGame(setWord, attempts, tip):
        global mask
        global word
        global err

        err = []

        dlg.check.setText("Checar")
        dlg.hit.setText("")
        dlg.hit.setText("")
        dlg.tip.setText(tip)
        dlg.errors.setText("")
        dlg.input.setPlaceholderText("ENTRE SUA TENTATIVA AQUI")
        dlg.input.setDisabled(False)
        # dlg.monkey.setPixmap(QtGui.QPixmap("full-monkey.png"))
        # pixmap = QtGui.QPixmap('full-monkey.png')
        # dlg.monkey.setText("Monkey")
        dlg.monkey.setPixmap(QtGui.QPixmap("src/hanggame/assets/macaco5.png"))
        # dlg.monkey.setPixmap(pixmap)
        # dlg.monkey.setScaledContents(True)
        

        word = setWord
        mask = '_'*len(word)
        dlg.life.setText(attempts)
        dlg.word.setText(letterSpacing(mask))

    def resetGame():
        txtWord, txtTip = getWord()
        setGame(txtWord, "5", txtTip)
        print("> Game reset")

    def checkInput(dlg):
        global word
        global mask
        global err

        if dlg.check.text() == "RESET": resetGame(); return
        userInput = dlg.input.toPlainText()
        life = int(dlg.life.text())



        if life == 0: noAttempt(dlg); clearInput(dlg); return
        if userInput == word: win(dlg, word); clearInput(dlg); return
        if userInput != word and len(userInput) > 1: wordWrong(dlg, life); clearInput(dlg); return
        if userInput == "": emptyInput(dlg); return

        if userInput in mask: AlreadyTypedLetter(dlg); clearInput(dlg); return
        else:
            hit, mask, err = checkWord(userInput, mask, word, err)
            dlg.word.setText(letterSpacing(mask))
            if mask == word: win(dlg, word); clearInput(dlg); return
            if not hit:
                falseHit(dlg, err)
                if (life == 1): lose(dlg, word)
                dlg.life.setText(str(life-1))
                eval(f'dlg.monkey.setPixmap(QtGui.QPixmap("src/hanggame/assets/macaco{dlg.life.text()}.png"))')
            if hit:
                trueHit(dlg)
            print("> Acertou:",hit)
            print("> Mascara:",mask)
            clearInput(dlg)

    dlg = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))
    QtGui.QFontDatabase.addApplicationFont("src/arcade.ttf")

    dlg.setStyleSheet('background-image : url(src/hanggame/assets/background.png);')
    word, mask, err = "", "", list()

    txtWord, txtTip = getWord()

    setGame(txtWord, "5", txtTip)

    dlg.check.clicked.connect(lambda: checkInput(dlg))

    dlg.show()
