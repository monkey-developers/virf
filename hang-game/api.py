from os import path
from random import randint

def falseHit(dlg, err):
    dlg.hit.setText("Missed")
    dlg.errors.setText(letterSpacing(err))
    pass

def trueHit(dlg):
    dlg.hit.setText("Hit!")
    pass

def lose(dlg):
    dlg.check.setText("Reset")
    print(">> You lose!")
    dlg.result.setText("YOU LOSE!")

def noAttempt():
    print("> Acabou suas tentativas");

def wordWrong(dlg):
    print("> Sua palavra não corresponde")
    dlg.hit.setText("Missed")

def AlreadyTypedLetter(dlg):
    print("> Você digitou essa letra")
    dlg.hit.setText("Already typed that letter")

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
    dlg.hit.setText("You didnt type anything")

def clearInput(dlg):
    dlg.input.setText("")

def letterSpacing(string):
    arr = list(string)
    return " ".join(arr)

def win(dlg, word):
    dlg.word.setText(letterSpacing(word))
    dlg.check.setText("Reset")
    print(">> You win!")
    dlg.result.setText("YOU WIN!")
    
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