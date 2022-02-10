# M - x axis width
# N - y axis height
# K - number of actions made by artist

#Each of these lines will either be R followed
#by a single space and then an integer which is a row number, or C followed by a single space
#and then an integer which is a column number. 

# variable for flipped rows
# variable for flipped collumns
# array for flipped rows
# array for flipped collumns
# counter for gold tiles

canvasWidth = int(input())
flippedRowsCount = 0
flippedRows = [0] * canvasWidth # 0 is unflipped, 1 is flipped
canvasHeight = int(input())
flippedCollumnsCount = 0
flippedCollumns = [0] * canvasHeight # 0 is unflipped, 1 is flipped
actionsTaken = int(input())

# gold = (number of collumns * collumn height) - number of rows 
# PLUS
# (number of rows * row length) - number of collumns

for i in range(0, actionsTaken):
    axisDesignation, rcNumber = [i for i in input().split()]
    rcNumber = int(rcNumber)
    if axisDesignation == "C" and flippedCollumns[rcNumber - 1] != 1:
        flippedCollumns[rcNumber - 1] = 1
        flippedCollumnsCount += 1
    elif axisDesignation == "C" and flippedCollumns[rcNumber - 1] == 1:
        flippedCollumns[rcNumber - 1] = 0
        flippedCollumnsCount -= 1
    elif axisDesignation == "R" and flippedCollumns[rcNumber - 1] != 1:
        flippedRows[rcNumber - 1] = 1
        flippedRowsCount += 1
    else:
        flippedRows[rcNumber - 1] = 0
        flippedRowsCount -= 1

goldTiles = 0
goldTiles = (flippedCollumnsCount * canvasHeight) - flippedRowsCount
goldTiles += (flippedRowsCount * canvasWidth) - flippedCollumnsCount
print(goldTiles)