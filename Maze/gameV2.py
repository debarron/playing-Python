from random import randint

MOVES = "Indicate a move[ U:Up D:Down R:Right L:Left ] => "
CURRENT_X = 0
CURRENT_Y = 0
GAME_ON = True
WRONG_MOVE = False

# World
ROWS = 4
COLS = 4
PITS = []
PITS_LEN = 5

def initPits():
    PITS = []
    count = 0

    while count < PITS_LEN:
        pitY = randint(0,ROWS)
        pitX = randint(0,COLS)

        found = False
        for pit in PITS:
            if pit[0] == pitY and pit[1] == pitX:
                found = True

        if found == False:
            count = count + 1
            PITS.append((pitY, pitX))

    print("###################")
    print("# PRINITNG THE PITS")
    for pit in PITS:
        print("PIT {0} {1}".format(pit[0], pit[1]))
    print("###################")

# Validate the move
def validateOption(move):
    if move == "U" or move == "D" or move == "L" or move == "R":
        return True
    else:
        return False

# This prints out the new X and Y
# We validate the move, sayin that if it's an invalid
# one, we might as well ignore it and print out a warning
def makeMove(move):
    newX = CURRENT_X
    newY = CURRENT_Y
    invalid = False

    if move == "U":
        newY = newY + 1
    elif move == "D":
        newY = newY - 1
    elif move == "R":
        newX = newX + 1
    elif move == "L":
        newX = newX - 1

    if (newX < 0 or newY < 0) or (newY > ROWS or newX > COLS): 
        newX = CURRENT_X
        newY = CURRENT_Y
        invalid = True
    
    return (newX, newY, invalid)

def printLocation():
    print(">> We're at: {0} {1}".format(CURRENT_Y, CURRENT_X))


# Game starts here
initPits()

while GAME_ON == True:
    printLocation()

    move = raw_input(MOVES)
    GAME_ON = validateOption(move)
    CURRENT_X, CURRENT_Y, WRONG_MOVE = makeMove(move)

    if WRONG_MOVE == True:
        print("=>> :$ Wrong move, nothing changes")
    elif WRONG_MOVE == False:
        failed = False
        closeToFail = False
        for pit in PITS:
            diff = abs(pit[0] - CURRENT_Y) + abs(pit[1] - CURRENT_X)
            print("The difference is: " + str(diff))

            if diff == 0:
                failed = True
                print("Failed into a pit")
            elif diff == 1:
                closeToFail = True
                print("Smell a pit")


