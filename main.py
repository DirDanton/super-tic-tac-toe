#Preparation
MainGame = []

def Winner(array):
    #Check for X
    for i in range(len(array)):
        if i <= 2: # vertical W check
            if array[i] == 'X':
                if array[i+3] == 'X' :
                    if array[i+6] == 'X':
                        return [True, 'X']
        if i == 0 or i == 3 or i == 6: # horizontal W check
            if array[i] == 'X':
                if array[i+1] == 'X':
                    if array[i+2] == 'X':
                        return [True, 'X']
        if i == 0:
            if array[i] == 'X':
                if array[i+4] == 'X':
                    if array[i+8] == 'X':
                        return [True, 'X']
        if i == 2:
            if array[i] == 'X':
                if array[i+2] == 'X':
                    if array[i+4] == 'X':
                        return [True, 'X']
    #Check for O
    for i in range(len(array)):
        if i <= 2: # vertical W check
            if array[i] == 'O':
                if array[i+3] == 'O' :
                    if array[i+6] == 'O':
                        return [True, 'O']
        if i == 0 or i == 3 or i == 6: # horizontal W check
            if array[i] == 'O':
                if array[i+1] == 'O':
                    if array[i+2] == 'O':
                        return [True, 'O']
        if i == 0:
            if array[i] == 'O':
                if array[i+4] == 'O':
                    if array[i+8] == 'O':
                        return [True, 'O']
        if i == 2:
            if array[i] == 'O':
                if array[i+2] == 'O':
                    if array[i+4] == 'O':
                        return [True, 'O']
    return [False]

for i in range(9):
    MainGame.append([])
    for i2 in range(9):
        MainGame[i].append(False)
    
def drawBoard(array):
    for i in range(3):
        string = ''
        for k in range(3):
            string = string + (array[i*3+k] or str(i*3+k))
            if not k == 2:
                string = string + ' | '
        print(string)
        
def drawGame():
    for v in range(3):
        for w in range(3):
            for x in range(3):
                string = ''
                for y in range(3):
                    for z in range(3):
                        string = string + (MainGame[v*3+y][w*3+z] or ' ')
                        if z < 2:
                            string = string + ' | '
                    if y < 2:
                        string = string + '  |  '
            print(string)
        print('-------------------------------------')

currentPlayer = True
currentSideGame = -1

def main(reDraw):
    global currentPlayer
    global currentSideGame
    player = False
    if currentPlayer:
        player = 'X'
    else:
        player = 'O'
    if currentSideGame == -1:
        # Let him select place to play
        currentSideGame2 = input("Choose a slot to start playing in (1 -> 9):")
        currentSideGame2 = int(currentSideGame2)
        winner = Winner(MainGame[currentSideGame2-1])
        if currentSideGame2 > 0 and currentSideGame2 < 10 and not winner[0]:
            currentSideGame = currentSideGame2 - 1
            main(True)
            return
        else:
            print('Error, this game is already won by: ' + winner[1])
            main(True)
            return
    if reDraw:
        print('You are playing as ' + player)
        drawBoard(MainGame[currentSideGame])
    nextPlay = input("Write the number of the box you want to play in:")
    try:
        if nextPlay == 'exit' or nextPlay == 'quit' or nextPlay == 'q':
            return
        elif nextPlay == 'show':
            drawGame()
            main(True)
            return
        nextPlay = int(nextPlay)
        if nextPlay > -1 and nextPlay < 9:
            if MainGame[currentSideGame][nextPlay]:
                print('Error, This box is already taken!')
                main(False)
                return
            MainGame[currentSideGame][nextPlay] = player
            currentPlayer = not currentPlayer
            currentSideGame = nextPlay
            if Winner(MainGame[currentSideGame])[0]:
                currentSideGame = -1
            main(True)
        else:
            print('Error, Invalid value. Range is 0 to 8')
            main(False)
            return
    except:
        print('Error, Invalid value. Use "exit", "quit", or "q" to quit.')
        main(False)
        return

main(True)