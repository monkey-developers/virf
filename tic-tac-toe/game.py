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
    
    # print(rows)
    # print(cols)
    # print(diag1)
    # print(diag2)
    
    def verify_list(arr):
        return all(element == arr[0] for element in arr)

    def verify_mtx(mtx):
        for b in range(3): 
            print(mtx[b]); 
            print(verify_list(mtx[b]))
        #for a in range(3):
            #win = verify_list(mtx[a])
        return False

    # if verify_list(diag1): print("Someone won")
    if verify_mtx(rows): print("Someone won")

    # if verify_list(diag1) or verify_list(diag2) or verify_mtx(rows) or verify_mtx(cols):
        #print("Someone won")

    if not '' in arr: print("Empate!"); reset()

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
    