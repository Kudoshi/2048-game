'''
1) addOneValue 'SETTLE'
2) DisplayBoard
3) Combine Value
4) Lose Screen
'''
import random


def setup():
    global boardList
    boardList = []

    # Insert manually the value
    for row in range(0, gridSize, 1):
        rowList = []
        for col in range(0, gridSize, 1):
            rowList.append(0)
        boardList.append(rowList)


def addOneValue():
    # Generate random number
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
    while True:
        if checkEmptyGrid() == True:
            addOneValue()
            print(boardList)
        else:
            break



# gridSize = int(input("Input grid size: "))
gridSize = 4

setup()
main()
topLine = "-" * (gridSize * 11) + "-"
horizontalLine = "|          |" + "          |" * (gridSize - 1)
itemLineExtra = f"{boardList[0][1]}".center(10) + "|"
itemLine = "|" + f"{boardList[0][1]}".center(10) + "|" + itemLineExtra * (gridSize - 1)
for i in range(0,4):
    print(topLine)
    print(horizontalLine)
    print(itemLine)
    print(horizontalLine)
print(topLine)

# print("----------")
# print("|        |")
# print("|  2048  |")
# print("|        |")
# print("----------")
# print("|        |")
# print("|  2048  |")
# print("|        |")
# print("----------")
# print("|        |")
# print("|  2048  |")
# print("|        |")
# print("----------")
# print("|        |")
# print("|  2048  |")
# print("|        |")
# print("----------")
