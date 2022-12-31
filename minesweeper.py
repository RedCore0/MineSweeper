import random
class tile():
    def __init__(self, covered, type, visual):
        self.covered = covered
        self.type = type
        self.visual = visual

TileASCII = ["   "," * "," F ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]
t = tile(True, " O ", "")
TileCord = [" A "," B "," C "," D "," E "," F "," G "," H "," I "]
board = []

def CreateBoard():
    y = 0 
    while y < 9:
        row = [] 
        x = 0
        while x < 9:
            row.append(tile(True, " - ", ""))
            x+=1
        board.append(row)
        y+=1
    mines = 0
    while mines < 10:
        RandY = random.randint(0, 8)
        RandX = random.randint(0, 8)
        RandRow = board[RandY]
        RandTile = RandRow[RandX]
        RandTile.type = TileASCII[1]
        mines+=1
    for X in board:
        i=0
        for Y in X:
            if Y.type == TileASCII[1]:
                if i != 0: X[i-1].type = TileASCII[3]
                if i+1 < len(X): X[i+1].type = TileASCII[3]
            i+=1

def PrintBoard():
    ReadableBoard = board
    for X in ReadableBoard:
        i = 0
        while i < len(X):
            X[i] = X[i].type
            i+=1
    print("   ", ''.join(TileCord))
    i = 0
    for ROW in ReadableBoard:
        print(TileCord[i], ''.join(ROW))
        i+=1      
CreateBoard()
PrintBoard()