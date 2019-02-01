from random import randint
import numpy

worldRows = 5
worldCols = 5

pits = {}
pitValue = 3
pitCount = 5

goldCoords = (0, 0)
goldValue = 2

monsterCoords = (0, 0)
monsterValue = 1


def coordsToKey(row, col):
    key = (row * (worldCols-1)) + col
    return key

def keyToCoords(key):
    row = int(key / worldCols -1)
    cols = key - row
    return (row, col)

####################################
# PRINTING
####################################
def printPits():
    for coords in pits:
	y, x = pits[coords]
	print("Pit at: " + str(x) + " " + str(y))



####################################
## INIT FUNCTIONS
####################################
def initPits():
    while(len(pits) < pitCount):
        row, col = 0 , 0

        while (row == 0 and col == 0):
            row = randint(0, 4)
	    col = randint(0, 4)

	key = coordsToKey(row, col)
	if not pits.has_key(key):
	    pits[key] = (row, col)

def initLocation():
    row = randint(0, 4)
    col = randint(0, 4)
    return (row, col)

def createWorld(rows, cols):
    return numpy.zeros((rows, cols))


# TODO Change the or for str_lowecase or similar
def newLocations(userLocation, move):
    row, col = userLocation
    if move == "U" or move == "u": 
        row = row + 1
    elif move == "D" or move == "d": 
        row = row - 1
    elif move == "L" or move == "l": 
        col = col - 1
    elif move == "R" or move == "r": 
        col = col + 1

    return (row, col)

####################################
# VALIDATIONS
####################################
# TODO Change the or for str_lowecase or something similar
def validMove(currentRow, currentCol, move):
    if (move == "U" or move == "u") and (currentRow == worldRows - 1): 
        return False
    elif (move == "D" or move == "d") and (currentRow == 0): 
        return False
    elif (move == "R" or move == "r") and (currentCol == worldCols - 1): 
        return False
    elif (move == "L" or move =="l") and (currentCol == 0): 
        return False
    else: 
        return True


def isGameFinish(userLocation, userHasGold, userAlive):
    y, x = userLocation
    if x == 0 and y == 0 and userHasGold == True and userAlive == True: 
        return True
    else: 
        return False

def isPitClose(currentLocation):
    y, x = currentLocation

    for key in pits:
        yp, xp = pits[key]
        rx = abs(xp - x)
        ry = abs(yp - y)
    
        if rx == 1 and ry == 1:
            return "I feel a breeze"

    return "Seams safe"

initPits()
monsterCoords = initLocation()
goldCoords = initLocation()
world = createWorld(worldRows, worldCols)
xg, yg = goldCoords
xm, ym = monsterCoords


# Locate elements in the map
world[xg][yg] = goldValue
world[xm][ym] = monsterValue
for coords in pits:
	px, py = pits[coords]
	world[px][py] = pitValue

initialCords = (0, 0)
userHasGold = False
userAlive = True

printPits()
print("Monster at: " + str(monsterCoords))
print("Monster at: " + str(goldCoords))

userRow, userCol = 0, 0
while not isGameFinish((userRow, userCol), userHasGold, userAlive):
    # Check if there is a pit close to your current location
    pitMessage = isPitClose((userRow, userCol))
    print("Regarding the pits, I think " + pitMessage)

    valid = False
    while not valid:
        command = raw_input("Where to move? (U:Up, D:Down, R:Right, L:Left): ")

        if (validMove(userRow, userCol, command)):    
           #Change this to str_lowercase or something similar
            if(command == "u" or command == "U"):
                userRow = userRow + 1
            elif(command == "d" or command == "D"):
                userRow = userRow - 1
            elif(command == "l" or command == "L"):
                userCol = userCol - 1
            elif(command == "r" or command == "R"):
                userCol = userCol + 1

            print(">>> Current location: " + str(userRow) + ", " + str(userCol))
            valid = True
        
        else:
            print("Incorrect option, try again please")
    
    '''
    command = raw_input("Where to move? (U:Up, D:Down, R:Right, L:Left): ")
    print("The command is: " + command)

    if (validMove(userRow, userCol, command)):    
        #Change this to str_lowercase or something similar
        if(command == "u" or command == "U"):
            userRow = userRow + 1
        elif(command == "d" or command == "D"):
            userRow = userRow - 1
        elif(command == "l" or command == "L"):
            userCol = userCol - 1
        elif(command == "r" or command == "R"):
            userCol = userCol + 1

        print("New coords are " + str(userRow) + " " + str(userCol))

    else:
        print("Invalid move")
    '''
    

'''
while not isGameFinish((userRow, userCol), userHasGold, userAlive):
    # Check if there is a pit close to your current location
    pitMessage = isPitClose((userRow, userCol))
    print("Regarding the pits, I think " + pitMessage)

    valid = False
    while not valid:
    
        command = raw_input("Where to move? (U:Up, D:Down, R:Right, L:Left): ")
        if validMove(userRow, userCol, command):
            y, x = newLocations((userRow, userCol), command)
            userRow, userCol = y, x
            print(">>> Current location: " + str(userRow) + ", " + str(userCol))
            valid = True
        else:
            print("Incorrect option, try again please")
'''


