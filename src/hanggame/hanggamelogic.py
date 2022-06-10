from os import path
from random import randint

from PyQt5 import QtGui

def falseHit(dlg, err):
    dlg.hit.setText("ERRO!")
    dlg.errors.setText(letterSpacing(err))
    pass

def trueHit(dlg):
    dlg.hit.setText("ACERTO!")
    pass

def lose(dlg, word):
    dlg.check.setText("RESET")
    dlg.word.setText(letterSpacing(word))
    dlg.hit.setText("GAME OVER")
    dlg.input.setPlaceholderText("VOCÊ PERDEU")
    dlg.input.setDisabled(True)

def noAttempt(dlg):
    dlg.hit.setText("ACABARAM SUAS TENTATIVAS");

def wordWrong(dlg, life):
    print("> Sua palavra não corresponde")
    dlg.hit.setText("PALAVRA ERRADA!")
    dlg.life.setText(str(life-1))
    eval(f'dlg.monkey.setPixmap(QtGui.QPixmap("src/hanggame/assets/macaco{dlg.life.text()}.png"))')

def AlreadyTypedLetter(dlg): dlg.hit.setText("JÁ DIGITADO")

def checkWord(userInput, mask, word, errorChars):
    correctCharIndex = list()
    hit = False

    for i, v in enumerate(list(word)): 
        if v == userInput: hit = True; correctCharIndex.append(i)

    if not hit: errorChars.append(userInput)

    maskList = list(mask)
    for j in correctCharIndex: maskList[j] = userInput
    return hit, "".join(maskList), errorChars

def emptyInput(dlg):
    dlg.hit.setText("DIGITE ALGO!")

def clearInput(dlg):
    dlg.input.setText("")

def letterSpacing(string):
    arr = list(string)
    return " ".join(arr)

def win(dlg, word):
    dlg.word.setText(letterSpacing(word))
    dlg.check.setText("RESET")
    dlg.hit.setText("VITORIA!")
    dlg.input.setDisabled(True)
    dlg.input.setPlaceholderText("VOCÊ VENCEU")
    
def getWord():
    script_dir = path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "words.txt"
    abs_file_path = path.join(script_dir, rel_path)
    f = open(abs_file_path, "r").read()
    row_arr = f.replace("\n", "").split(";")
    randow_row = row_arr[randint(0, len(row_arr) - 1)]
    word = randow_row.split(":")[0]
    tip = randow_row.split(":")[1]

    # word = randow_row.split(":")[0]
    # tip = randow_row.split(":")[1]
    return word, tip