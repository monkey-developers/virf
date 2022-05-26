from os import system, path
from PyQt5 import uic, QtWidgets, QtGui
import sys
from api import *

def setGame(setWord, attempts, tip):
    global mask
    global word
    global err

    err = list()

    dlg.check.setText("Check")
    dlg.result.setText("")
    dlg.hit.setText("")
    dlg.tip.setText(tip)
    # dlg.monkey.setPixmap(QtGui.QPixmap("full-monkey.png"))
    # pixmap = QtGui.QPixmap('full-monkey.png')
    dlg.monkey.setText("Monkey")
    # dlg.monkey.setPixmap(pixmap)
    # dlg.monkey.setScaledContents(True)
    

    word = setWord
    mask = '_'*len(word)
    dlg.life.setText(attempts)
    dlg.word.setText(letterSpacing(mask))


def resetGame():
    txtWord, txtTip = getWord()
    setGame(txtWord, "3", txtTip)
    print("> Game reset")

def checkInput(dlg):
    global word
    global mask
    global err

    if dlg.check.text() == "Reset": resetGame(); return
    userInput = dlg.input.toPlainText()
    life = int(dlg.life.text())

    if life == 0: noAttempt(); clearInput(dlg); return
    if userInput == word: win(dlg, word); return
    if userInput != word and len(userInput) > 1: wordWrong(dlg); clearInput(dlg); return
    if userInput == "": emptyInput(dlg); return

    if userInput in mask: AlreadyTypedLetter(dlg); clearInput(dlg); return
    else:
        hit, mask, err = checkWord(userInput, mask, word, err)
        dlg.word.setText(letterSpacing(mask))
        if mask == word: win(dlg, word)
        if not hit:
            falseHit(dlg, err)
            if (life == 1): lose(dlg)
            dlg.life.setText(str(life-1))
        if hit:
            trueHit(dlg)
        print("> Acertou:",hit)
        print("> Mascara:",mask)
        clearInput(dlg)

app = QtWidgets.QApplication([])
dlg = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))

word, mask, err = "", "", list()

txtWord, txtTip = getWord()

setGame(txtWord, "3", txtTip)

dlg.check.clicked.connect(lambda: checkInput(dlg))

dlg.show()
app.exec()