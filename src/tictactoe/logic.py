player = None
gameUi = None

def playAgain():
    global gameUi
    gameUi.startButton.show()
    gameUi.resetButton.hide()
    gameUi.label.setText("JOGAR NOVAMENTE?")


def reset():
    global player, gameUi
    player = None
    for i in range(9): eval('gameUi.button{}.clicked.disconnect()'.format(i))
    # gameUi.startButton.show()
    gameUi.resetButton.show()
    gameUi.resetButton.clicked.connect(playAgain)


def is_game_end():
    global gameUi, player
    arr = list()
    rows = list()
    row = list()
    for i in range(9):
        buttonText = eval('gameUi.button{}.text()'.format(i))
        arr.append(buttonText)
        row.append(buttonText)
        if i == 2 or i == 5 or i == 8: rows.append(row); row = []

    cols = list()
    for j in range(3):
        col = list()
        for k in range(3): col.append(rows[k][j])
        cols.append(col)
        
    diag1 = list()
    for l in range(3): diag1.append(rows[l][l])
    
    diag2 = list()
    inverted_rows = list(reversed(rows))
    for m in range(3): diag2.append(inverted_rows[m][m])
    
    def verify_list(arr):
        if (arr[0] == '' or arr[1] == '' or arr[2] == ''): return False
        return all(element == arr[0] for element in arr)

    def verify_mtx(mtx):
        for b in range(3):
            if (verify_list(mtx[b])): return True
        return False

    if not '' in arr: 
        gameUi.label.setText("Empate!!"); 
        reset()
    else:
        if verify_list(diag1) or verify_list(diag2) or verify_mtx(rows) or verify_mtx(cols):
            togglePlayer()
            gameUi.label.setText(f"Jogador {player} venceu!")
            reset()
        
        else: gameUi.label.setText(f"VEZ DO JOGADOR {player}")

def togglePlayer():
    global player, gameUi
    if player == "X": player = "O"
    else : player = "X"

def turn(pos):
    global player, gameUi
    print(">Position:", pos)
    print(">Player:", player)
    eval('gameUi.button{}.setText("{}")'.format(pos, player))
    eval('gameUi.button{}.setEnabled(False)'.format(pos))
    togglePlayer()
    is_game_end()

def setup(ui):
    global player, gameUi
    player = "X"
    gameUi = ui
    gameUi.label.setText(f"VEZ DO JOGADOR {player}")
    for i in range(9):
        eval('gameUi.button{}.setText("")'.format(i))
        eval('gameUi.button{}.setEnabled(True)'.format(i))
        eval('gameUi.button{}.clicked.connect(lambda: turn({}))'.format(i, i))
    