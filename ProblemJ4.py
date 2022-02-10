# by mattias and marco (example)
bookOrder = input()
numOrder = []
newBookOrder = []

count = 0

correctOrder = False

for x in range(0,len(bookOrder)):
    if bookOrder[x] == "L":
        numOrder.append(3)
    elif bookOrder[x] == "M":
        numOrder.append(2)
    elif bookOrder[x] == "S":
        numOrder.append(1)

# numOrder is the array containing the "bookshelf"
# where L = 3, M = 2, and S = 1

while correctOrder == False:
    c = 0
    for x in range(0,len(numOrder)-1):
        if numOrder[x] < numOrder[x + 1]:
            z = numOrder[x]
            numOrder[x] = numOrder[x + 1]
            numOrder[x + 1] = z
            count = count + 1

# numOrder organized
    for x in range(0,len(numOrder)-1):
        if numOrder[x] < numOrder[x+1]:
            print("bing")
            break
        if c == (len(numOrder) - 2):
            print("wong")
            correctOrder = True
        else:
            c = c + 1
    
print(count)
        

print(numOrder)

for element in numOrder:
    if element == 1:
        newBookOrder.append("S")
    elif element == 2:
        newBookOrder.append("M")
    elif element == 3:
        newBookOrder.append("L")


print(newBookOrder)
print(count)    

