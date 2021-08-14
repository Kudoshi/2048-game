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
    for i in range(0,10):
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
    for col in range(0, gridSize):
        # Initial bottom grid
        bottomGrid = boardList[gridSize - 1][col]
        # Get bottomGrid value
        if bottomGrid == 0:
            for row in range(gridSize - 2, -1, 1):
                upperValue = boardList[row][col]
                if upperValue != 0:
                    boardList[bottomGrid][col] = upperValue
                    upperValue = 0
                    break
        # Check if bottom grid is still 0 after getting value
        if bottomGrid == 0:
            continue
        for row in range(gridSize-2, -1, -1):
            upperValue = boardList[row][col]
            if upperValue != 0:
                aboveGrid = boardList[row-1][col]
                if bottomGrid == upperValue:
                    result = bottomGrid+upperValue
                    bottomGrid = result

        # IF bottomGrid has uppervalue
        # # Move down values
        #     FOR uppervalue IN range(gridSize-2,-1,-1)
        #         IF uppervalue has value
        #             SET aboveGrid = bottomGrid-1
        #             If bottomGrid == upperValue
        #                         ADD two together
        #                         Place result at bottomGrid
        #                         Delete uppervalue
        #             ELIF upperValue == aboveGrid
        #                 SET bottomgrid AS uppervalue
        #                 # uppervalue -= 1
        #             ELIF aboveGrid == 0
        #                 SET aboveGrid AS upperGrid
        #             ELSE
        #                 DO NOTHING
        #
        #         ELIF uppervalue no value
        #             CONTINUE




# FOR col IN RANGE(0,gridSize,1)
#     SET bottomGrid = gridSize-1
#     # Get the first uppervalue down to bottomgrid
#     IF bottomGrid has no value
#         for uppervalue IN range(gridSize - 2,-1,1)
#             if uppervalue is not 0
#                 SET bottomGrid AS uppergrid
#                 DELETE uppervalue
#                 BREAK
#         # If still no value
#         CONTINUE
#
#







# gridSize = int(input("Input grid size: "))
gridSize = 4

setup()
main()
displayBoard()




