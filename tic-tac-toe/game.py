player = None
gameUi = None

def reset():
    global player, gameUi
    player = None
    for i in range(9): eval('gameUi.button{}.clicked.disconnect()'.format(i))
    gameUi.startButton.show()

def is_game_end():
    global gameUi
    end = False
    arr = list()
    for i in range(9):
        buttonText = eval('gameUi.button{}.text()'.format(i))
        arr.append(buttonText)

    if not '' in arr: print("Empate!"); reset()

    print(arr)

def turn(pos):
    global player, gameUi
    print(">Position:", pos)
    print(">Player:", player)
    eval('gameUi.button{}.setText("{}")'.format(pos, player))
    eval('gameUi.button{}.setEnabled(False)'.format(pos))

    if player == "X": player = "O"
    else : player = "X"

    is_game_end()

def setup(ui):
    global player, gameUi
    player = "X"
    gameUi = ui
    for i in range(9):
        eval('gameUi.button{}.setText("")'.format(i))
        eval('gameUi.button{}.setEnabled(True)'.format(i))
        eval('gameUi.button{}.clicked.connect(lambda: turn({}))'.format(i, i))
    