import os
import sys
import json


def printToJson(path):
    arr = os.listdir(path)
    jsonFile = open("champions.json", "w+")
    cnt = 1
    jsonFile.write("[" + "\n")
    for x in arr:
        name = clearName(x)
        champ = {"id": (cnt-1), "name": name, "icon": path + "/" + x + '"'}
        jsonFile.write(json.dumps(champ, indent=2) + ",")
        cnt += 1
    jsonFile.write("]" + "\n")
    jsonFile.close()


def printToConsole(path):
    arr = os.listdir(path)
    cnt = 1
    print("[" + "\n")
    for x in arr:
        name = clearName(x)
        champ = {"id": (cnt-1), "name": name, "icon": path + "/" + x + ""}
        print(json.dumps(champ, indent=2) + ",")
        cnt += 1
    print("]" + "\n")


def printNamesOnly(path):
    arr = os.listdir(path)
    txtFile = open("namesOnly.txt", "w+")
    for x in arr:
        name = clearName(x)
        txtFile.write(name + "\n")
    txtFile.close()


def genTextLine(valName, value, lastLine):
    line = ""
    doubleTabSpace = "\t\t"
    laneBreak = "\n"
    line = doubleTabSpace + valName + ":" + value
    if lastLine == False:
        line += ","
    line += laneBreak
    return line


def clearName(fullName):
    name = fullName.replace("Square", "", 1).replace("_Original", "", 1).replace(
        " (1)", "", 1).replace(".png", "", 1).replace("_", " ", 1).replace("-27", "'", 1)
    return name


def start():
    argsLen = len(sys.argv)
    if argsLen == 1:
        path = input("Enter path or name of subfolder: ")
        os.system("cls")
        consOptions()
        inpt = int(input("Choose wisely: "))
        genWork(path, inpt)
    elif argsLen == 2:
        path = str(sys.argv[1])
        consOptions()
        inpt = int(input("Choose wisely: "))
        genWork(path, inpt)
    elif argsLen == 3:
        path = str(sys.argv[1])
        inpt = int(sys.argv[2])
        genWork(path, inpt)


def consOptions():
    print("1 = Print names only")
    print("2 = Print to json file")
    print("3 = Print to console")
    print("4 = Exit")
    print("")


def genWork(path, inpt):
    if inpt == 1:
        printNamesOnly(path)
        input("Press any key to exit")
    elif inpt == 2:
        printToJson(path)
        input("Press any key to exit")
    elif inpt == 3:
        printToConsole(path)
        input("Press any key to exit")
    elif inpt == 4:
        quit()
    else:
        os.system("cls")
        start()


start()
