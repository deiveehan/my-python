def writeFile(yippieCount):
    f1 = open("yippie.out", "w")
    f1.write(yippieCount)
    f1.close()

def readFile():
    f1 = open("yippie.out", "r")
    yippieCountStr = f1.read()
    f1.close()
    return yippieCountStr

processFlag = True
inputVal = ""
while processFlag:
    inputVal = str(input("Whats going on: "))
    yippieCountStr = readFile()
    if inputVal == "bing":
        yippieCount = int(yippieCountStr)
        yippieCount = yippieCount + 1
        writeFile(str(yippieCount))
        print("yippieCount : " + str(yippieCount))
    elif inputVal == "exit" or inputVal == "quit":
        processFlag = False

