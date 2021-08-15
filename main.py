'''
1) addOneValue 'SETTLE'
2) DisplayBoard 'SETTLE'
3) Movement & Combine Value
4) Lose Screen
'''
import random
import keyboard
import time
import os

def clearConsole():
    '''
    Clear console. Only works on terminal.
    Else it will next line to simulate clear
    '''
    print('\n'*200)
    cmd = "clear"
    if os.name in ('dos', 'nt'):
        cmd = "cls cmd"

    os.system(cmd)
    print("="*70)
def setup():
    global boardList
    boardList = []

    # Insert manually the value 0 into all cell
    for row in range(0, gridSize, 1):
        rowList = []
        for col in range(0, gridSize, 1):
            rowList.append(0)
        boardList.append(rowList)


def addOneValue():
    # Generate random number 2 or 4
    chances = random.randint(1, 10)
    if chances <= 5:
        value = 2
    else:
        value = 4

    # Insert value. If random place is filled. Find other place
    while True:
        # Generate random place
        ranRow = random.randint(0, gridSize - 1)
        ranCol = random.randint(0, gridSize - 1)

        # Check if value is filled
        if boardList[ranRow][ranCol] == 0:
            boardList[ranRow][ranCol] = value  # fill the 0 with value 2 or 4
            global newValueGrid
            newValueGrid = [ranRow,ranCol]
            break
        else:
            continue


def checkEmptyGrid():
    for row in range(0, gridSize, 1):
        for col in range(0, gridSize, 1):
            if boardList[row][col] == 0:
                return True
    return False


def main():
    clearConsole()
    addOneValue()
    addOneValue()
    global newValueGrid
    newValueGrid = None

    gameContinue = True
    while True:
        clearConsole()
        print("[ESCAPE] to main menu [ARROW KEYS] to move tiles".center(70))
        print("")
        print(f"SCORE: {score}".center(70)+"\n")

        displayBoard()



        if checkLose() == True:
            print("YOU LOSE")
            print("\nENTER ANY KEY TO CONTINUE".center(70))
            while True:
                if keyboard.read_key():
                    break
            return

        # Get user input
        while True:
            # check valid movement
            if keyboard.is_pressed('down'):
                move = "down"
                break
            elif keyboard.is_pressed('up'):
                move = "up"
                break
            elif keyboard.is_pressed('left'):
                move = "left"
                break
            elif keyboard.is_pressed('right'):
                move = "right"
                break
            elif keyboard.is_pressed('esc'):
                gameContinue = False
                break

        #Return to main menu
        if gameContinue == False:
            break

        #Check for valid input
        if movement(move, True) == True:
            movement(move)
        else:
            continue

        # Add values
        if checkEmptyGrid() == True:
            addOneValue()

        time.sleep(0.3)


def displayBoard():
    # Horizontal
    horizontalLine = "-" * (gridSize * 11) + "-"
    # Vertical
    verticalLine = "|          |" + "          |" * (gridSize - 1)
    # Set row and col value
    for row in range(0, gridSize):
        print(horizontalLine)
        print(verticalLine)
        # Change content value
        contentText = ""
        for col in range(0, gridSize):
            # On first column
            if col == 0:
                # If grid empty
                if boardList[row][col] == 0:
                    contentText += "|" + " ".center(10) + "|"
                else:
                    if newValueGrid != None and row == newValueGrid[0] and col == newValueGrid[1]:
                        contentText += "|" + f"( {boardList[row][col]} )".center(10) + "|"
                    else:
                        contentText += "|" + f"{boardList[row][col]}".center(10) + "|"
            # Not on first column
            else:
                if boardList[row][col] == 0:
                    contentText += " ".center(10) + "|"
                else:
                    if newValueGrid != None and row == newValueGrid[0] and col == newValueGrid[1]:
                        contentText += f"( {boardList[row][col]} )".center(10) + "|"
                    else:
                        contentText += f"{boardList[row][col]}".center(10) + "|"
        print(contentText)
        print(verticalLine)
    print(horizontalLine)

def checkLose():
    checkList = []
    checkList.append(movement("left",True))
    checkList.append(movement("right",True))
    checkList.append(movement("down",True))
    checkList.append(movement("up",True))

    if not True in checkList:
        return True

def movement(movement, checkOnly = False):
    global score
    def checkLockedGrid(searchRow,col):
        for element in lockedGridList:
            if element[0] == searchRow and element[1] == col:
                return True
    #Get movement information
    if movement == "down":
        colRange = [0,gridSize,1] #Update sequence left to right
        rowRange = [gridSize-2, -1, -1] #Comparison grid move up
        searchRowRange = [1, gridSize, 1] #Search down. Current row +1 get down
    elif movement == "up":
        colRange = [0, gridSize, 1]  # Left to right col
        rowRange = [1, gridSize, 1]  # Comparison grid move down
        searchRowRange = [-1, -1, -1]  # Search up.  Current row - 1 get up.
    elif movement == "left":
        colRange = [1,gridSize,1] #Comparison grid move right
        rowRange = [0,gridSize,1] #Update sequence top to bottom
        searchColRange = [-1,-1,-1] #Search left. Current col - 1 get left
    elif movement == "right":
        colRange = [gridSize-2,-1,-1] #Comparison grid move left
        rowRange = [0,gridSize,1] #Update sequence top to bottom
        searchColRange = [1, gridSize, 1] #Search right Current col +1 get up

    #Actual movement
    if movement == "left" or movement == "right":
        for row in range(rowRange[0], rowRange[1], rowRange[2]):
            lockedGridList = []

            for col in range(colRange[0], colRange[1], colRange[2]):
                # Check if comparingGrid is empty
                if boardList[row][col] == 0:
                    continue

                currentEmptyGrid = None
                comparingGridCombined = False

                # Search through the grids below
                for searchCol in range(col + searchColRange[0], searchColRange[1], searchColRange[2]):
                    # Check if the searched grid is in the lockedGridList
                    if checkLockedGrid(row, searchCol) == True:
                        break

                    # Check if the searched grid is empty
                    if boardList[row][searchCol] == 0:
                        currentEmptyGrid = [row, searchCol]
                        continue
                    # Check if searchGrid's value is matches the comparingGrid
                    elif boardList[row][searchCol] == boardList[row][col]:
                        if checkOnly == True:
                            return True
                        comparingGridCombined = True
                        result = boardList[row][searchCol] + boardList[row][col]
                        boardList[row][searchCol] = result
                        boardList[row][col] = 0
                        score += result
                        lockedGridList.append([row, searchCol])
                    else:
                        break

                # Check if no combination was made. Pull comparisonGrid to searchGrid
                if comparingGridCombined == False and currentEmptyGrid != None:
                    if checkOnly == True:
                        return True
                    boardList[currentEmptyGrid[0]][currentEmptyGrid[1]] = boardList[row][col]
                    boardList[row][col] = 0

    if movement == "up" or movement == "down":
        for col in range(colRange[0], colRange[1], colRange[2]):
            #For each row before the end of grid. Descending order
            # print("Column Number: ", col)
            lockedGridList = []  # [ [3,1],[]]
            for row in range(rowRange[0], rowRange[1], rowRange[2]):
                #Check if comparingGrid is empty
                if boardList[row][col] == 0:
                    continue

                currentEmptyGrid = None
                comparingGridCombined = False

                #Search through the grids below
                for searchRow in range(row + searchRowRange[0], searchRowRange[1],searchRowRange[2]):
                    #Check if the searched grid is in the lockedGridList
                    if checkLockedGrid(searchRow,col) == True:
                        break

                    #Check if the searched grid is empty
                    if boardList[searchRow][col] == 0:
                        currentEmptyGrid = [searchRow,col]
                        continue
                    #Check if searchGrid's value matches the comparingGrid
                    elif boardList[searchRow][col] == boardList[row][col]:
                        if checkOnly == True:
                            return True
                        comparingGridCombined = True
                        result = boardList[searchRow][col] + boardList[row][col]
                        boardList[searchRow][col] = result
                        boardList[row][col] = 0
                        score += result
                        lockedGridList.append([searchRow,col])
                    else: #Break searching if encounters a value that doesn't match.
                        break

                #Check if no combination was made
                if comparingGridCombined == False and currentEmptyGrid != None:
                    if checkOnly == True:
                        return True
                    boardList[currentEmptyGrid[0]][currentEmptyGrid[1]] = boardList[row][col]
                    boardList[row][col] = 0

    if checkOnly == True: #Returns false if it has not return true yet
        return False


while True:
    clearConsole()
    print("By Kudoshi and Bright".center(70))
    print("___________".center(70))
    print("Welcome to 2048 Game".center(70))
    print("_"*70+"\n")
    print("                              Decision:")
    print("[PLAY] Play game".center(70))
    print("[EXIT] Exit Game".center(70))
    print("\n"+"_"*70)
    while True:
        decision = input("\nInput your decision:").upper()
        if decision == "PLAY":
            while True:
                try:
                    gridSize = int(input("Input board size [2-6]: "))
                    if gridSize < 2 or gridSize > 6:
                        print("Invalid board size. Try again")
                        continue
                    else:
                        break
                except:
                    print("Invalid board size input. Try again")
                    continue
            #START
            #START
            score = 0
            newValueGrid = None
            setup()
            main()
            #END
            break
        elif decision == "EXIT":
            exit()
        else:
            print("Invalid Input. Try again")