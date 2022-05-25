from os import system, path
from PyQt5 import uic, QtWidgets

from api import game

def win():
    dlg.word.setText(word)
    print(">> You win!")

def lose():
    print(">> You lose!")

def noAttempt():
    print("> Acabou suas tentativas");

def wordWrong():
    print("> Sua palavra não corresponde")

def AlreadyTypedLetter():
    print("> Você digitou essa letra")

def checkWord(userInput, mask):
    correctCharIndex = list()
    errorChars = list()
    hit = False

    for i, v in enumerate(list(word)): 
        if v == userInput: hit = True; correctCharIndex.append(i)

    if not hit: errorChars.append(userInput)

    maskList = list(mask)
    for j in correctCharIndex: maskList[j] = userInput
    return hit, "".join(maskList)

def emptyInput():
    print("> You didnt type anything")

def clearInput():
    dlg.input.setText("")

def checkInput():
    global word
    global mask
    userInput = dlg.input.toPlainText()
    life = int(dlg.life.text())

    if life == 0: noAttempt(); clearInput(); return
    if userInput == word: win(); return
    if userInput != word and len(userInput) > 1: wordWrong(); clearInput(); return
    if userInput == "": emptyInput(); return

    if userInput in mask: AlreadyTypedLetter(); clearInput(); return
    else:
        hit, mask = checkWord(userInput, mask)
        dlg.word.setText(mask)
        if not hit:
            print("> errastes")
            if (life == 1): lose()
            dlg.life.setText(str(life-1))
        if mask == word: win()
        print("> Acertou:",hit)
        print("> Mascara:",mask)
        clearInput()


app = QtWidgets.QApplication([])
dlg = uic.loadUi(path.join(path.dirname(__file__), "screen.ui"))

word = "banana"
mask = '_'*len(word)
err = list()

dlg.life.setText('6')
dlg.word.setText(mask)

dlg.check.clicked.connect(checkInput)

dlg.show()
app.exec()