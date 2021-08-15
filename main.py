'''
1) addOneValue 'SETTLE'
2) DisplayBoard 'SETTLE'
3) Movement & Combine Value
4) Lose Screen
'''
import random


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
    # Fill the grid with value
    for i in range(0,2):
        if checkEmptyGrid() == True:
            addOneValue()

        else:
            break
    print(boardList)


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
                    contentText += "|" + f"{boardList[row][col]}".center(10) + "|"
            # Not on first column
            else:
                if boardList[row][col] == 0:
                    contentText += " ".center(10) + "|"
                else:
                    contentText += f"{boardList[row][col]}".center(10) + "|"
        print(contentText)
        print(verticalLine)
    print(horizontalLine)


def movementDown():
    def checkLockedGrid(searchRow,col):
        for element in lockedGridList:
            if element[0] == searchRow and element[1] == col:
                return True
    #Set movement values for the loops

    for col in range(0, gridSize):
        #For each row before the end of grid. Descending order
        print("Column Number: ", col)
        lockedGridList = []  # [ [3,1],[]]
        for row in range(gridSize-2, -1, -1):
            #Check if comparingGrid is empty
            if boardList[row][col] == 0:
                continue

            currentEmptyGrid = None
            comparingGridCombined = False


            #Search through the grids below
            for searchRow in range(row+1, gridSize,1):
                #Check if the searched grid is in the lockedGridList
                if checkLockedGrid(searchRow,col) == True:
                    break

                #Check if the searched grid is empty
                if boardList[searchRow][col] == 0:
                    currentEmptyGrid = [searchRow,col]
                    continue
                #Check if searchGrid's value is matches the comparingGrid
                elif boardList[searchRow][col] == boardList[row][col]:
                    comparingGridCombined = True
                    result = boardList[searchRow][col] + boardList[row][col]
                    boardList[searchRow][col] = result
                    boardList[row][col] = 0

                    lockedGridList.append([searchRow,col])

            #Check if no combination was made
            if comparingGridCombined == False and currentEmptyGrid != None:
                boardList[currentEmptyGrid[0]][currentEmptyGrid[1]] = boardList[row][col]
                boardList[row][col] = 0




# # gridSize = int(input("Input grid size: "))
gridSize = 4

setup()
main() #Input some random values rn
displayBoard()

for i in range(1,100,1):
    print("current loop: ",i)

    if checkEmptyGrid() == True:
        addOneValue()
        movementDown()
        displayBoard()
    else:
        break

print("GameOver")