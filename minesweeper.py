import random
import copy
class tile():
    def __init__(self, covered, type, visual, MinesAround):
        self.covered = covered
        self.type = type
        self.visual = visual
        self.MinesAround = MinesAround

TileASCII = ["   "," * "," F ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]
#t = tile(True, " O ", "")
TileCord = [" A "," B "," C "," D "," E "," F "," G "," H "," I "]
CommandCord = ["A","B","C","D","E","F","G","H","I"]
board = []

def CreateBoard():
    y = 0 
    while y < 9:
        row = [] 
        x = 0
        while x < 9:
            row.append(tile(True, "   ", " - ", 3))
            x+=1
        board.append(row)
        y+=1
    mines = 0
    while mines < 9:
        RandY = random.randint(0, 8)
        RandX = random.randint(0, 8)
        RandRow = board[RandY]
        RandTile = RandRow[RandX]
        if RandTile.type != TileASCII[1]:
            RandTile.type = TileASCII[1]
            mines+=1
    if mines == 9:
        NumberBoard()
    

def NumberBoard():
    j=0
    for X in board:
        i=0
        for Y in X:
            if Y.type == TileASCII[1]:
                if i != 0 and X[i-1].type != TileASCII[1]:
                    X[i-1].type = TileASCII[X[i-1].MinesAround]
                    X[i-1].MinesAround += 1 
                if i+1 < len(X) and X[i+1].type != TileASCII[1]:
                    X[i+1].type = TileASCII[X[i+1].MinesAround]
                    X[i+1].MinesAround += 1
                
                if j != 0:
                    Upper = board[j-1] 
                    if Upper[i].type != TileASCII[1]:
                        Upper[i].type = TileASCII[Upper[i].MinesAround]
                        Upper[i].MinesAround +=1
                    if Upper[i-1].type != TileASCII[1] and i != 0:
                        Upper[i-1].type = TileASCII[Upper[i-1].MinesAround]
                        Upper[i-1].MinesAround +=1
                    if i+1 < len(X) and Upper[i+1].type != TileASCII[1]:
                        Upper[i+1].type = TileASCII[Upper[i+1].MinesAround]
                        Upper[i+1].MinesAround +=1
                
                
                if j+1 < len(board):
                    Lower = board[j+1]
                    if Lower[i].type != TileASCII[1]:
                        Lower[i].type = TileASCII[Lower[i].MinesAround]
                        Lower[i].MinesAround +=1
                    if Lower[i-1].type != TileASCII[1] and i != 0:
                        Lower[i-1].type = TileASCII[Lower[i-1].MinesAround]
                        Lower[i-1].MinesAround += 1
                    if i+1 < len(X) and Lower[i+1].type != TileASCII[1]:
                        Lower[i+1].type = TileASCII[Lower[i+1].MinesAround]
                        Lower[i+1].MinesAround += 1
            i+=1
        j+=1

def UserActionController(input):
    row = input[0]; col = input[2]; act = input[4]
    colID = 0; rowID = 0
    
    count = 0
    for i in CommandCord:
        if col == i: colID = count
        if row == i: rowID = count
        count+=1
    SelectedColumn = board[colID]
    SelectedTile = SelectedColumn[rowID]
    SelectedTile.covered = False

    if SelectedTile.type == TileASCII[0]:
        RowCheck = 1
        while colID-RowCheck >= 0:
            UpperAdjacent = board[colID-RowCheck]
            UpperAdjacent[rowID].covered = False
            if UpperAdjacent[rowID].type == TileASCII[0]:
                ColumnCheck = 1
                while rowID-ColumnCheck >= 0:
                    SideAdjacent = UpperAdjacent[rowID-ColumnCheck]
                    SideAdjacent.covered = False
                    if SideAdjacent.type == TileASCII[0]: ColumnCheck+=1
                    else: ColumnCheck = 9999
                RowCheck +=1
            else: RowCheck = 9999

    PrintBoard()

def PrintBoard():
    ReadableBoard = copy.deepcopy(board)
    print("               ('‿')")
    print("   ", ''.join(TileCord))
    i = 0
    for ROW in ReadableBoard:
        z = 0
        for Tile in ROW:
            if Tile.covered == False: ROW[z] = Tile.type; z+=1
            else: ROW[z] = Tile.visual; z+=1
        print(TileCord[i], ''.join(ROW))
        i+=1
    ReadableBoard.clear()
    print("Actions: C to Check   F to Flag \nType: <Row> <Column> <Action>")
    PLayerConsole = input("/")
    UserActionController(PLayerConsole)

CreateBoard()
PrintBoard()