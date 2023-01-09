#==========================================================================================================================================================================
#   Minesweeper game
#   Made by Michal Redzko
#
#                                                           !!!First section of the code!!! 
#
#   This part of the code firstly imports necessary modules
#
#   This section of the code contains a class called "tile". objects of that class are used to create the board
#
#   Last thing located in this code sections are instances of lists and variables that are used in multiple functions
#
#
#                                                            !!!CreateBoard Function!!!
#
#   This function runs at the start of the game
#   CreateBoard function contains user input which allows user to select difficulty level
#   This function prints board of appropriate size based on chosen difficulty
#   it aslo spawns mines in random places on the board
#   When board is created and mines are placed NumberBoard function is activated
# 
#
#                                                           !!!NumberBoard Function!!!
# 
#   This function counts how many mines are around a certain tile and numbers it appropriately
#   Firstly id finds tiles with mines
#   Then it checks all the adjacent tiles
#   tile objects have "MinesAround" property which is an integer
#   when code finds out there is a mine next to a tile, this tile's MinesAround is increased by 1
#   this process is repeated with every tile that has a mine assigned to it
#   When board is fully setup PrintBoard function is activated
#
#
#                                                          !!!PrintBoard Function!!!
#
#   This function is responsible for displaying almost everything to the player
#   UI is printed in 3 stages
#   Firstly the number of flags and emoji
#   emoji displays game's condition, Smiling face means the game continues, 
#       Dead emoji means the game is lost and Sunglasses emoji means the player won.
#   then the column coordinates are printed. Coordinates are displayed alphabetically
#   this gives better contrast between playing space and coordinates
#   In Second Stage board itself is printed
#   Each row is given a coordinate similarly to columns
#   Lastly in third stage further instructions and input area are printed
#   Based on the game's state this area is different
#   if the game is lost player only gets the option to restart
#   if the game is won player is given an option to write his name and publish his score to a leaderboard
#   if the game still continues player is able to interact with the board
#   Possible commands are displayed and all the basic instruction on how to write them are shown with example
#   When player types in a command to place flag or open a tile UserInteractionController function is activated
#
#
#                                                      !!!UserInteractionController!!!
#   
#
#   This function is responsible for opening and flagging the tiles selected by the player
#   if player wants to open a tile it sets tile's covered property to False displaying what's underneath it
#   if selected uncovered tile has no mines around adjacent tiles are checked
#   Then adjecent tiles of tiles adjacent to uncovered tile are checked and so on.
#   This process repeats itself until all empty tiles connected to uncovered tile are opened
#   if Player wants to flag a tile code checks is specific contidions are met
#   those are if tile is not opened and if tile is not already flagged
#   when those conditions are met flag is placed
#   when there is already a flag on the tile that flag is removed
#   In this part of code the number of correct guesses is also checked
#   If player has correctly guessed where all the mines are located then player wins
#
#==================================================================================================================================================================================

#Final Build


#Imports all requiered modules
import random
import time

#This class creates a tile object type
#Covered is a bool if true tile is not opened, else it is
#type is a string. it represents a layer of what's under the tile. so cues and mines
#visual is a string. it represents the surface. so unopened tiles and flags
#MinesAround is an integer. This integer holds the number of mines surrounding a tile
class tile():
    def __init__(self, covered, type, visual, MinesAround):
        self.covered = covered
        self.type = type
        self.visual = visual
        self.MinesAround = MinesAround

#here the global variables and lists are instantiated
TileASCII = ["   "," * "," F ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]
TileCord = [" A "," B "," C "," D "," E "," F "," G "," H "," I ", " J ", " K ", " L ", " M ", " N ", " O ", " P ", " Q ", " R ", " S ", " T ", " U ", " V ", " W ", " X ", " Y ",
" Z ", " a ", " b ", " c ", " d ", " e ", " f ", " g "]
CommandCord = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g"]
board = []
Flags = 10
Lost = False
Win = False
Time = time.time()

DifficultyLevel = ""
DifficultyLevelForScoreBoard = ["Beginner", "Intermediate", "Expert"]
MinesAmount = 0
MinesFound = 0
ColumnSize = 0

#This function asks the player to choose difficulty level
#Then it creates a 2d array of tiles that player will later be able to iunteract with
def CreateBoard():

    #Here player is asked to choose difficulty based on that board size
    #and amount of mines is being set. 
    ############################################################################
    global DifficultyLevel; global MinesAmount; global ColumnSize; global Flags; global MinesFound
    MinesFound = 0
    Continue = False
    while Continue == False:
        print("b = Beginner    i = Intermediate    e = Expert")
        DifficultyLevel = input("/")
        if DifficultyLevel == "b":
            RowSize = 9; ColumnSize = 9; MinesAmount = 10; Flags = 10; Continue = True
        elif DifficultyLevel == "i":
            RowSize = 16; ColumnSize = 16; MinesAmount = 40; Flags = 40; Continue = True
        elif DifficultyLevel == "e":
            RowSize = 30; ColumnSize = 16; MinesAmount = 99; Flags = 99; Continue = True
        else: print("unknown command")
    ##############################################################################
      
    #This while loop creates a 2d array of tiles with parameters set by chosen difficulty level
    #################################################
    y = 0 
    while y < RowSize:
        row = [] 
        x = 0
        while x < ColumnSize:
            row.append(tile(True, "   ", " - ", 3))
            x+=1
        board.append(row)
        print(len(board))
        y+=1
    ##################################################

    #This piece of code places mines in random locations on the board
    ##############################################
    mines = 0
    while mines < MinesAmount:
        RandY = random.randint(0, RowSize-1)
        RandX = random.randint(0, ColumnSize-1)
        RandRow = board[RandY]
        RandTile = RandRow[RandX]
        if RandTile.type != TileASCII[1]:       #Checks if randomly selected tile doesn't already have a mine
            RandTile.type = TileASCII[1]
            mines+=1
    if mines == MinesAmount:
        NumberBoard()   #When all mines are placed this function is activated
    ###############################################

#This function checks the amount of mines surrounding a tile and places cues approprietly
def NumberBoard():
    #Those for loops go through every tile and execute the code within them when tile contains a mine
    j=0
    for X in board:
        i=0
        for Y in X:
            if Y.type == TileASCII[1]:
                #setup cue on the tile left and right from the mine 
                if i != 0 and X[i-1].type != TileASCII[1]:
                    X[i-1].type = TileASCII[X[i-1].MinesAround]
                    X[i-1].MinesAround += 1 
                if i+1 < len(X) and X[i+1].type != TileASCII[1]:
                    X[i+1].type = TileASCII[X[i+1].MinesAround]
                    X[i+1].MinesAround += 1
                
                #setup cue on tiles located on top and top corners from the mine
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
                
                #setup cue on tiles located on bottom and bottom corners from the mine
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

#This function takes Player's board interaction command and edits board based on that
def UserActionController(input):
    #this piece of code dissects player's command into coordinates and action
    row = input[0]; col = input[2]; act = input[4]
    colID = 9999; rowID = 9999
    global Flags
    AllowUncover = False
    count = 0
    for i in CommandCord:
        if col == i: colID = count
        if row == i: rowID = count
        count+=1
    
    #If coordinates given by player exist this if statement is ctivated 
    if colID < len(board) and rowID < len(board):         
        SelectedColumn = board[colID]
        SelectedTile = SelectedColumn[rowID]

        #if player wants to open the tile this if statement is activated
        if act == "C" and SelectedTile.visual != TileASCII[2]:
            SelectedTile.covered = False
            AllowUncover = True
            #If selected tile has mine it sets the game's state to Lost
            if SelectedTile.type == TileASCII[1]:
                global Lost; Lost = True
        
        #if Player wants to flag or remove flag from the tile this if statement is activated
        if act == "F" and SelectedTile.covered == True:
            if SelectedTile.visual == " - ": SelectedTile.visual = TileASCII[2]; Flags-=1
            elif SelectedTile.visual == TileASCII[2]: SelectedTile.visual = " - "; Flags+=1

    #When player opens the tile this if statement is activated 
    #here  when opened tile is empty it uncovers the adjacent tiles
    if AllowUncover == True:
        ToUncover = [] #This list holds all tiles that will be uncovered
        if(SelectedTile.type == TileASCII[0]): #this if statement adds adjacent empty tiles to be checked
            ToUncover.append(SelectedTile)
        
        #This while loop goes through every empty tile connected to selected tile and opens their neighbouring tiles
        ToUncoverUpdated = 0
        while ToUncoverUpdated < len(ToUncover): 
            for CurrentTile in ToUncover:
                for i in board:
                    if CurrentTile in i:
                        CurrentColumn = i
                #Checks tiles on the left and right from a tile from ToUncover list
                #those tiles are opened
                #if those tiles are empty they are added to ToUncover list
                #if there's flag on them the flag gets removed
                #those stepps are repeated for all adjacent tiles
                if CurrentColumn.index(CurrentTile) != 0:
                    CheckLeft = CurrentColumn.index(CurrentTile)-1
                    if CurrentColumn[CheckLeft].type == TileASCII[0] and CurrentColumn[CheckLeft].covered == True:
                        ToUncover.append(CurrentColumn[CheckLeft])
                    CurrentColumn[CheckLeft].covered = False
                    if CurrentColumn[CheckLeft].visual == TileASCII[2]: Flags+=1;CurrentColumn[CheckLeft].visual=""
                if CurrentColumn.index(CurrentTile)+1 < len(CurrentColumn):
                    CheckRight = CurrentColumn.index(CurrentTile)+1
                    if CurrentColumn[CheckRight].type == TileASCII[0] and CurrentColumn[CheckRight].covered == True:
                        ToUncover.append(CurrentColumn[CheckRight])
                    CurrentColumn[CheckRight].covered = False
                    if CurrentColumn[CheckRight].visual == TileASCII[2]: Flags+=1;CurrentColumn[CheckRight].visual=""

                #Checks tiles on the top and top corners from tile from ToUncover list
                if board.index(CurrentColumn) != 0:
                    TopInt = board.index(CurrentColumn)-1
                    Top = board[TopInt]
                    if Top[CurrentColumn.index(CurrentTile)].type == TileASCII[0] and Top[CurrentColumn.index(CurrentTile)].covered == True:
                        ToUncover.append(Top[CurrentColumn.index(CurrentTile)])
                    Top[CurrentColumn.index(CurrentTile)].covered = False
                    if Top[CurrentColumn.index(CurrentTile)].visual == TileASCII[2]: Flags+=1;Top[CurrentColumn.index(CurrentTile)].visual=""
                    
                    TopL = Top.index(Top[CurrentColumn.index(CurrentTile)])
                    if TopL != 0:
                        TopLeft = Top[CurrentColumn.index(CurrentTile)-1]
                        if TopLeft.type == TileASCII[0] and TopLeft.covered == True:
                            ToUncover.append(TopLeft)
                        TopLeft.covered = False
                        if TopLeft.visual == TileASCII[2]: Flags+=1;TopLeft.visual=""

                    if TopL+1 < len(CurrentColumn):
                        TopRight = Top[CurrentColumn.index(CurrentTile)+1]
                        if TopRight.type == TileASCII[0] and TopRight.covered == True:
                            ToUncover.append(TopRight)
                        TopRight.covered = False
                        if TopRight.visual == TileASCII[2]: Flags+=1;TopRight.visual=""
                
                #Checks tiles on the bottom and bottom corners from tile from ToUncover list
                if board.index(CurrentColumn)+1 < len(board):
                    BottomInt = board.index(CurrentColumn)+1
                    Bottom = board[BottomInt]
                    if Bottom[CurrentColumn.index(CurrentTile)].type == TileASCII[0] and Bottom[CurrentColumn.index(CurrentTile)].covered == True:
                        ToUncover.append(Bottom[CurrentColumn.index(CurrentTile)])
                    Bottom[CurrentColumn.index(CurrentTile)].covered = False
                    if Bottom[CurrentColumn.index(CurrentTile)].visual == TileASCII[2]:Flags+=1;Bottom[CurrentColumn.index(CurrentTile)].visual=""

                    BottomTiles = Bottom.index(Bottom[CurrentColumn.index(CurrentTile)])
                    if BottomTiles != 0:
                        BottomLeft = Bottom[CurrentColumn.index(CurrentTile)-1]
                        if BottomLeft.type == TileASCII[0] and BottomLeft.covered == True:
                            ToUncover.append(BottomLeft)
                        BottomLeft.covered = False
                        if BottomLeft.visual == TileASCII[2]: Flags+=1;BottomLeft.visual=""

                    if BottomTiles+1 < len(CurrentColumn):
                        BottomRight = Bottom[CurrentColumn.index(CurrentTile)+1]
                        if BottomRight.type == TileASCII[0] and BottomRight.covered == True:
                            ToUncover.append(BottomRight)
                        BottomRight.covered = False
                        if BottomRight.visual == TileASCII[2]: Flags+=1;BottomRight.visual=""
                ToUncoverUpdated+=1
    
    #This piece of code checks if all tiles with mines are flagged if yes then Player wins
    ######################################################################
    global MinesAmount
    global MinesFound

    MinesFound = 0
    for Row in board:
        for Tile in Row:
            if Tile.visual == TileASCII[2] and Tile.type == TileASCII[1]:
                print("Running")
                MinesFound+=1
    if MinesFound == MinesAmount:
        global Win; Win = True
    ######################################################################
    
    PrintBoard() # Print edited board

#This function prints UI that player can interact with
def PrintBoard():
    print("\033[H\033[J")   #Clears the terminal
    #Gets global variables
    ###########
    global Lost
    global Win
    global Flags
    global Time
    global ColumnSize
    ###########
    ReadableBoard = list(map(list, board)) #Creates a copy of a board 
    HorizontalCords = TileCord.copy()  #Creates a copy of Tile coordinates(List With Alphabet)
    PrintableCords = []
    
    #Creates a list that will be printed as horizontal coordinates
    for Column in HorizontalCords:
        if HorizontalCords.index(Column) >= ColumnSize:
            Column = ""
        PrintableCords.append(Column)

    #This code checks the game state and determines which emoji to print
    ###################################################
    emojis = ["     ('‿')", "     (*_*)","    (⌐■_■)"]
    emoji=""
    if Lost == True: emoji = emojis[1]
    elif Win == True: emoji = emojis[2]
    else: emoji = emojis[0]
    ###################################################
    
    #Prints stuff above the board
    print("Flags:",Flags, emoji)
    print("   ", ''.join(PrintableCords))
    
    #this for loop goes through every tile checks it's state and based on that
    #prints board appropriately
    ############################################################################
    i = 0
    for ROW in ReadableBoard:
        z = 0
        for Tile in ROW:
            if Tile.covered == False: ROW[z] = Tile.type; z+=1
            elif Lost == False:
                ROW[z] = Tile.visual; z+=1
            else:
                if Tile.type == TileASCII[1]: ROW[z] = Tile.type; z+=1
                elif Tile.visual != TileASCII[2]: ROW[z] = Tile.visual; z+=1
                else: Tile.visual = " X "; ROW[z] = Tile.visual; z+=1
        print(TileCord[i], ''.join(ROW))
        i+=1
    ReadableBoard.clear()
    ############################################################################

    ### This if else statement checks game's state ###
    if Lost == True:
        #From here player can restart the game by typing in correct command
        print("!!!  GAME OVER  !!!\ntype 'restart' To play again")
        while Lost == True:
            PLayerConsole = input("/")
            if PLayerConsole == "restart":
                board.clear()
                Lost=False
                Flags = 10
                Time = time.time()
                CreateBoard()
                PrintBoard()
            else: print("Unknown Command")
    elif Win == True:
        #From here player can write down his name and save his score
        global DifficultyLevel
        Difficulty = ""
        if DifficultyLevel == "b": Difficulty = DifficultyLevelForScoreBoard[0]
        elif DifficultyLevel == "i": Difficulty = DifficultyLevelForScoreBoard[1]
        else: Difficulty = DifficultyLevelForScoreBoard[2]
        print("!!!  YOU WIN  !!!\nTime:", round(time.time()-Time)," Seconds")
        UserName = input("What's your name?")
        
        ### !!! WARNING !!! ###
        #This code works as intended in VScode terminal
        #However when I tested it by running python file it didn't work
        # I assume it's something to do with the directory of my python 3.10 app
        # might work as intended on other computers when running python file
        
        #This creates or if already exists edits a text file with score board
        ScoreBoard = open("ScoreBoard.txt", "a+")        
        ScoreText = UserName, "        ",Difficulty,"       ", str(round(time.time()-Time))        
        ScoreBoard.writelines(ScoreText)
        ScoreBoard.write("\n ")

        #Restarts the game
        exit()
    else:
        Continue = False
        print("Actions: C to Check   F to Flag\n(!!!CAPS SENSITIVE!!!) e.g:/A B F\nType: /<Column> <Row> <Action>   or  /hint")
        while Continue == False:
            PLayerConsole = input("/")
            if PLayerConsole == "hint": #hint command finds a tile with undiscovered mine and puts a flag on it
                for Row in board:
                    for Tile in Row:
                        if Tile.type == TileASCII[1] and Tile.visual != TileASCII[2]:
                            Tile.visual = TileASCII[2]
                            Flags-=1
                            global MinesFound; MinesFound+=1
                            if MinesFound == MinesAmount: Win=True
                            PrintBoard()
            elif len(PLayerConsole) >=5: #if command is long enough to be detected as interation command action controller is activated
                UserActionController(PLayerConsole); Continue = True
            else: print("Unknown Command") #if command is unkown this lets player know
                

        
CreateBoard()
PrintBoard()