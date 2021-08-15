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


def movementDown(movement):
    def checkLockedGrid(searchRow,col):
        for element in lockedGridList:
            if element[0] == searchRow and element[1] == col:
                return True
    #Get movement
    if movement == "Down":
        colRange = [0,gridSize,1] #Update sequence left to right
        rowRange = [gridSize-2, -1, -1] #Comparison grid move up
        searchRowRange = [1, gridSize, 1] #Search down. Current row +1 get down
    elif movement == "Top":
        colRange = [0, gridSize, 1]  # Left to right col
        rowRange = [1, gridSize, 1]  # Start from second from top, go down
        searchRowRange = [-1, -1, -1]  # Search up.  Current row - 1 get up.
    elif movement == "Left":
        colRange = [1,gridSize,1] #Comparison grid move right
        rowRange = [0,gridSize,1] #Update sequence top to bottom
        searchColRange = [-1,-1,-1] #Search left. Current col - 1 get left
    elif movement == "Right":
        colRange = [gridSize-2,-1,-1] #Comparison grid move left
        rowRange = [0,gridSize,1] #Update sequence top to bottom
        searchColRange = [1, gridSize, 1] #Search right Current col +1 get up

    #Actual movement
    if movement == "Left" or movement == "Right":
        for row in range(rowRange[0], rowRange[1], rowRange[2]):
            print("Row Number: ", row)
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
                        comparingGridCombined = True
                        result = boardList[row][searchCol] + boardList[row][col]
                        boardList[row][searchCol] = result
                        boardList[row][col] = 0

                        lockedGridList.append([row, searchCol])
                    else:
                        break

                # Check if no combination was made
                if comparingGridCombined == False and currentEmptyGrid != None:
                    boardList[currentEmptyGrid[0]][currentEmptyGrid[1]] = boardList[row][col]
                    boardList[row][col] = 0

    if movement == "Top" or movement == "Down":
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
                        comparingGridCombined = True
                        result = boardList[searchRow][col] + boardList[row][col]
                        boardList[searchRow][col] = result
                        boardList[row][col] = 0

                        lockedGridList.append([searchRow,col])
                    else: #Break searching if encounters a value that doesn't match.
                        break

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
        print("ADDING ONE VALUE")
        addOneValue()
        displayBoard()
        print("MOVEMENT DOWN")
        movement = input("Input movement: ")
        movementDown(movement)
        displayBoard()
    else:
        break

print("GameOver")
