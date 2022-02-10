# If their sum is odd, then the direction to turn is left.
# If their sum is even and not zero, then the direction to turn is right.
# If their sum is zero, then the direction to turn is the same as the previous instruction.

outputDirection = []
outputSteps = []
count = 0

check = False
while check == False:
    num = input()
    if int(num) == 99999:
        check = True       
    else:
        num = [int(i) for i in str(num)]
        twoDigitSum = num[0] + num[1]
        if twoDigitSum % 2 != 0:
            direction = "left"
        elif twoDigitSum % 2 == 0 and twoDigitSum != 0:
            direction = "right"
        numberSteps = str(num[2]) + str(num[3]) + str(num[4])
        outputDirection.append(direction)
        outputSteps.append(numberSteps)
        count += 1

for i in range(0, count):
    print(outputDirection[i], outputSteps[i])