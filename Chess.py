## Imports librarys used in the program
import pygame
import os
import pickle

## Initialises pygame
pygame.init()

## Sets the size of the display and the caption to use
display_x = 1200
display_y = 800
gamedisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('Chess')

## Loads all necessary images
light_tile = pygame.image.load('img/light_wood.jpg')
dark_tile = pygame.image.load('img/dark_wood.jpg')
red_highlight = pygame.image.load('img/red_square.png')
blue_highlight = pygame.image.load('img/blue_square.png')
black_king = pygame.image.load('img/black_king.png')
black_queen = pygame.image.load('img/black_queen.png')
black_castle = pygame.image.load('img/black_castle.png')
black_bishop = pygame.image.load('img/black_bishop.png')
black_knight = pygame.image.load('img/black_knight.png')
black_pawn = pygame.image.load('img/black_pawn.png')
white_king = pygame.image.load('img/white_king.png')
white_queen = pygame.image.load('img/white_queen.png')
white_castle = pygame.image.load('img/white_castle.png')
white_bishop = pygame.image.load('img/white_bishop.png')
white_knight = pygame.image.load('img/white_knight.png')
white_pawn = pygame.image.load('img/white_pawn.png')

## Sets value of rgb colours to variables
white = (200, 200, 200)
button_1 = (50, 50, 50)
button_2 = (100, 100, 100)

## Sets the font style and size
myfont = pygame.font.SysFont("monospace", 25)
## sets the text and colour to a variable
load_text = myfont.render("Load", 1, white)
save_text = myfont.render("Save", 1, white)
exit_text = myfont.render("Exit", 1, white)
reset_text = myfont.render("Reset", 1, white)
queen_text = myfont.render("Queen", 1, white)
bishop_text = myfont.render("Bishop", 1, white)
castle_text = myfont.render("Castle", 1, white)
knight_text = myfont.render("Knight", 1, white)
white_win_text = myfont.render("White Wins!", 1, button_1)
black_win_text = myfont.render("Black Wins!", 1, button_1)

## Draws the basic 8x8 board of chess
def board():
    tile_type = True
##  Loops through all the x co-ordinate values
    for i in range (0, 8):
##      Loops through all the y co-ordinate values
        for j in range (0, 8):
##          Multiplies the x and y values by 100 so the represent real co-ordinates on screen (800pxx800px board)
            x = i * 100
            y = j * 100
##          Selects light or dark tile based on boolean to create checkered effect
            if tile_type == True:
##              Displays dark tile at the looped x and y co-ordinates  
                gamedisplay.blit(dark_tile, (x,y)) 
            else:
##              Displays light tile at the looped x and y co-ordinates  
                gamedisplay.blit(light_tile, (x,y))
##          Switches boolean so other tile is selected next to create checkered effect 
            tile_type = not tile_type
##      Switches boolean so other tile starts next x column for checkered effect  
        tile_type = not tile_type

def buttons():
##  stores position of mouse
    mouse_hover = pygame.mouse.get_pos()
##  Determines if mouse is hovering over the location of a button, if it is a lighter colour is provided to indicate the button is interactive 
    if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 100 and mouse_hover[1] <= 200:
        pygame.draw.rect(gamedisplay, button_2, (900, 100, 200, 100))
    else:
        pygame.draw.rect(gamedisplay, button_1, (900, 100, 200, 100))

    if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 300 and mouse_hover[1] <= 400:
        pygame.draw.rect(gamedisplay, button_2, (900, 300, 200, 100))
    else:
        pygame.draw.rect(gamedisplay, button_1, (900, 300, 200, 100))

    if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 500 and mouse_hover[1] <= 600:
        pygame.draw.rect(gamedisplay, button_2, (900, 500, 200, 100))
    else:
        pygame.draw.rect(gamedisplay, button_1, (900, 500, 200, 100))

    if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 700 and mouse_hover[1] <= 800:
        pygame.draw.rect(gamedisplay, button_2, (900, 700, 200, 100))
    else:
        pygame.draw.rect(gamedisplay, button_1, (900, 700, 200, 100))

##  Displays text ontop of the buttons
    gamedisplay.blit(load_text, (970, 140))
    gamedisplay.blit(save_text, (970, 340))
    gamedisplay.blit(exit_text, (970, 540))
    gamedisplay.blit(reset_text, (965, 740))

## Defines what occurs if the load button is pressed
def load(white_pieces, black_pieces, white_turn):
##  Checks file exists 
    if os.path.isfile("Save.p") == True:
##      gets the list from the file and stores it 
        saved_game = pickle.load( open("Save.p", "rb"))
##      using the data in the file the pieces are set to the loaded games position and the players turn is also set back to whos it was
        white_pieces = saved_game[0]
        black_pieces = saved_game[1]
        white_turn = saved_game[2]
    return white_pieces, black_pieces, white_turn
    

## Defines what occurs if the save button is pressed   
def save(white_pieces, black_pieces, white_turn):
##  Stores game information into one list
    saved_game = [white_pieces, black_pieces, white_turn]
##  Checks is a save game already exists, if it does then the file is deleted so a new one can be created
    if os.path.isfile("Save.p") == True:
        os.remove("Save.p")
##  Stores the game data in a new pickle file
    pickle.dump( saved_game, open("Save.p", "wb"))

## Defines what occurs if the reset button is pressed. All game data is reset back to its starting values.
def reset(white_pieces, black_pieces, white_turn, checkmate):
    black_pieces = [["K", 300, 0, False], ["Q", 400, 0], ["C", 0, 0, False], ["C", 700, 0, False], ["B", 200, 0], ["B", 500, 0], ["Kn", 100, 0], ["Kn", 600, 0], ["P", 0, 100, False],
                ["P", 100, 100, False], ["P", 200, 100, False], ["P", 300, 100, False], ["P", 400, 100, False], ["P", 500, 100, False], ["P", 600, 100, False],
                ["P", 700, 100, False]]
    white_pieces = [["K", 300, 700, False], ["Q", 400, 700], ["C", 0, 700, False], ["C", 700, 700, False], ["B", 200, 700], ["B", 500, 700], ["Kn", 100, 700], ["Kn", 600, 700], ["P", 0, 600, False],
                ["P", 100, 600, False], ["P", 200, 600, False], ["P", 300, 600, False], ["P", 400, 600, False], ["P", 500, 600, False], ["P", 600, 600, False],
                ["P", 700, 600, False]]
    white_turn = True
    checkmate = False
    return white_pieces, black_pieces, white_turn, checkmate
    

## Draws chess pieces onto board, correct images are passed through as parameters based on if the black pieces or the white are being inserted on screen
def draw_pieces(pieces, king, queen, castle, bishop, knight, pawn):
##  Loops through entite list of chess pieces  
    for k in range(0, len(pieces)):
##      Based on the first element of the embedded list the correct image is selected and the second and third elements are used to display on the correct tile  
        if pieces[k][0] == "K":
            gamedisplay.blit(king, (int(pieces[k][1]),int(pieces[k][2])))
        elif pieces[k][0] == "Q":
            gamedisplay.blit(queen, (int(pieces[k][1]),int(pieces[k][2])))
        elif pieces[k][0] == "C":
            gamedisplay.blit(castle, (int(pieces[k][1]),int(pieces[k][2])))
        elif pieces[k][0] == "B":
            gamedisplay.blit(bishop, (int(pieces[k][1]),int(pieces[k][2])))
        elif pieces[k][0] == "Kn":
            gamedisplay.blit(knight, (int(pieces[k][1]),int(pieces[k][2])))
        elif pieces[k][0] == "P":
            gamedisplay.blit(pawn, (int(pieces[k][1]),int(pieces[k][2])))

## Defines what occurs during a players turn
def turn(pieces, opponent, moveable_tiles, tile_x, tile_y, white_turn, piece_selected, selected_piece, checkmate):
    
##  If no previous piece has been selected then this section is used to determine if the player has selected one of their pieces  
    if piece_selected == False:
##      Loops through all of the player pieces  
        for m in range(0, len(pieces)):          
##          Compares if the mouse click was on the same tile as one of the players pieces 
            if tile_x == pieces[m][1] and tile_y == pieces[m][2]:
                delete_marker = []
                del delete_marker[:]
                opponent_location = []
                del opponent_location[:]
##              Defines what happens if the selected piece is a pawn
                if pieces[m][0] == "P":
##                  As pawns can only move forward two different dictionary entries are reuired to decide direction. Based on whose turn it is the correct dictionary entry is called.
                    if white_turn == True:
##                      Sets variable to the correct list of where the piece can move if its a white pawn, using the movement dictionary
                        direction = movement["WP"]
                    elif white_turn == False:
##                      Sets variable to the correct list of where the piece can move if its a black pawn
                        direction = movement["BP"]
##                  Adds the tile in front of the pawn to the list which contains all co-ordinates where the piece can move
                    moveable_tiles.append([tile_x, (tile_y + direction[0][1]), False, None])
##                  Checks if pawn has moved before
                    if pieces[m][3] == False:
##                      Adds the tile two spaces in front of the pawn if it has not moved before
                        moveable_tiles.append([tile_x, (tile_y + (direction[0][1])*2), False, None])
##                  Calls function to check if any of the players pieces are on the same tile as where the piece can move, or if a move is out of bounds   
                    obsticle_check(pieces, moveable_tiles, pieces[m], delete_marker)
##                  Calls function to check if any of the opponents pieces are on the same tile as where the piece can move, or if a move is out of bounds 
                    obsticle_check(opponent, moveable_tiles, pieces[m], delete_marker)
##                  Loops through all opponent pieces
                    for s in range(0, len(opponent)):
##                      Loops through all the attack moves of the pawn  
                        for u in range(1, 3):
##                          Checks if an opponents piece is in the attack tile of a pawn
                            if (tile_x + direction[u][0]) == opponent[s][1] and (tile_y + direction[u][1]) == opponent[s][2]:
##                              Adds a possible attack move to a list to be added to the moveable_tiles after the loop is finished
                                opponent_location.append([(tile_x + direction[u][0]), (tile_y + direction[u][1]), True, s])
##              Defines what happens if the selected piece is a knight
                elif pieces[m][0] == "Kn":
##                  Sets variable to the correct list of where the piece can move if its a knight, using the movement dictionary
                    direction = movement["Kn"]
##                  Calls function to determine where the knight can move
                    king_knight_movement(direction, moveable_tiles, delete_marker, opponent, tile_x, tile_y)
##                  Calls function to check if any of the players pieces are on the same tile as where the piece can move, or if a move is out of bounds  
                    obsticle_check(pieces, moveable_tiles, pieces[m], delete_marker)
##              Defines what happens if the selected piece is a king
                elif pieces[m][0] == "K":
##                  Sets variable to the correct list of where the piece can move if its a king, using the movement dictionary
                    direction = movement["K"]
##                  Calls function to determine where the king can move
                    king_knight_movement(direction, moveable_tiles, delete_marker, opponent, tile_x, tile_y)
##                  Calls function to check if any of the players pieces are on the same tile as where the piece can move, or if a move is out of bounds 
                    obsticle_check(pieces, moveable_tiles, pieces[m], delete_marker)
##              Defines what happens if the selected piece is a castle
                elif pieces[m][0] == "C":
##                  Sets variable to the correct list of where the piece can move if its a castle, using the movement dictionary
                    direction = movement["C"]
##                  Calls function to determine where the castle can move, eliminating illegal moves and also adding attacks
                    castle_bishop_queen_movement(pieces, opponent, moveable_tiles, direction, tile_x, tile_y)
##              Defines what happens if the selected piece is a bishop
                elif pieces[m][0] == "B":
##                  Sets variable to the correct list of where the piece can move if its a bishop, using the movement dictionary
                    direction = movement["B"]
##                  Calls function to determine where the bishop can move, eliminating illegal moves and also adding attacks
                    castle_bishop_queen_movement(pieces, opponent, moveable_tiles, direction, tile_x, tile_y)
##              Defines what happens if the selected piece is a queen
                elif pieces[m][0] == "Q":
##                  Sets variable to the correct list of where the piece can move if its a queen, using the movement dictionary
                    direction = movement["Q"]
##                  Calls function to determine where the queen can move, eliminating illegal moves and also adding attacks
                    castle_bishop_queen_movement(pieces, opponent, moveable_tiles, direction, tile_x, tile_y)
##              Loops through list so any marked moves can be deleted from the list
                for t in range(0, len(delete_marker)):
##                  Deletes move from list if its marked as invalid  
                    del moveable_tiles[delete_marker[t]]
##                  When a delete occurs all delete markers and reduced by 1 as all the indexing will have shifted by -1
                    for y in range(0, len(delete_marker)):
                        delete_marker[y] = delete_marker[y] - 1
##              Loops through all marked attacks and adds them to the valid moves list
                for v in range(0, len(opponent_location)):
                    moveable_tiles.append(opponent_location[v])


##              Sets the variable to true so next button click the other part of the function runs
                piece_selected = True
##              Stores the index of the selected piece
                selected_piece = m
##              Breaks from for loop
                break

##  If a piece has been selected then this section of the function runs
    elif piece_selected == True:
##      Loops through all the highlighted tiles
        for p in range(0, len(moveable_tiles)):
##          if the mouse click is on a highlighted tile this section runs  
            if tile_x == moveable_tiles[p][0] and tile_y == moveable_tiles[p][1]:
##              Changes the selected pieces co-ordinates to the highighted cell
                pieces[selected_piece][1] = moveable_tiles[p][0]
                pieces[selected_piece][2] = moveable_tiles[p][1]
##              If the piece moved was a pawn it is marked as moved so it can not move two spaces again
                if moveable_tiles[p][2] == True:
                    del opponent[moveable_tiles[p][3]]
##              If the piece was a pawn it is marked as moved
                if pieces[selected_piece][0] == "P":
                    pieces[selected_piece][3] = True
##                  Checks if pawn has reached the end of the board, if it has function is run  
                    if pieces[selected_piece][2] == 0 or pieces[selected_piece][2] == 700:
                        pieces = pawn_change(selected_piece, pieces)
##              If a piece is moved the other players go is intiated
                white_turn = not white_turn
                break
##      Resets the variables so the highlights disappear and changes boolean value so the other section of the function can run  
        del moveable_tiles[:]
        piece_selected = False
##      Sets the win condition to true
        checkmate = True
##      Loops through all of opponents pieces 
        for c in range(0, len(opponent)):
##          If the king piece is still there the win condition is set to false
            if opponent[c][0] == "K":
                checkmate = False       
##  returns boolean values to be used in other sections of the program   
    return white_turn, piece_selected, selected_piece, checkmate

## Checks if any pieces are in the way of a move or if a move is out of bounds               
def obsticle_check(check_pieces, moveable_tiles, selected_piece, delete_marker):
##  Loops through all saved moves 
    for q in range(0, len(moveable_tiles)):
##      Loops through the list of pieces it has to check the moves against
        for r in range(0, len(check_pieces)):
##          Checks if a possible move has the same co-ordinates as a piece already there  
            if moveable_tiles[q][0] == check_pieces[r][1] and moveable_tiles[q][1] == check_pieces[r][2]:
##              If the move is on the same tile as a piece then the index number of the move is stored to be deleted later  
                delete_marker.append(q)
##              If the piece is a pawn, it hasn't moved before and the tile infront of it has been marked as invalid, this also marks the tile above it as invalid for later deletion   
                if q == 0 and selected_piece[0] == "P" and selected_piece[3] == False:
                    delete_marker.append(q+1)
##      If the move uses co-ordinates outside the bounds of the game it is marked for later deletion
        if moveable_tiles[q][0] > 700 or moveable_tiles[q][0] < 0 or moveable_tiles[q][1] > 700 or moveable_tiles[q][1] < 0:
            delete_marker.append(q)

##  Defines where a knight or king can move and attack      
def king_knight_movement(direction, moveable_tiles, delete_marker, opponent, tile_x, tile_y):
##  Loops through all available directions   
    for w in range(0, len(direction)):
##      Adds the new move to the list
        moveable_tiles.append([tile_x + direction[w][0], tile_y + direction[w][1], False, None])
##      Loops through all opponent locations  
        for x in range(0, len(opponent)):
##          If an opponent is on the same tile as teh move, the element is changes to acknowledge its an attack
            if tile_x + direction[w][0] == opponent[x][1] and tile_y + direction[w][1] == opponent[x][2]:
                moveable_tiles[w][2] = True
                moveable_tiles[w][3] = x

## Defines where castles, knights and queens can move and attack
def castle_bishop_queen_movement(pieces, opponent, moveable_tiles, direction, tile_x, tile_y):
##  Loops through each direction the piece can move
    for z in range(0, len(direction)):
##      Resets the variables back to where the piece is and initiates while loop
        start_x = tile_x
        start_y = tile_y
        cont = True
        while cont == True:
##          Loops through where all player pieces are 
            for a in range(0, len(pieces)):
##              If a piece is on the same tile as the next move then the while loop is broken 
                if ((start_x + direction[z][0]) == pieces[a][1] and (start_y + direction[z][1]) == pieces[a][2]) or (start_x + direction[z][0]) > 700 or (start_x + direction[z][0]) < 0 or (start_y + direction[z][1]) > 700 or (start_y + direction[z][1]) < 0:
                    cont = False
##          Loops through where all the opponent pieces are  
            for b in range(0, len(opponent)):
##              If a piece is on the same tile as the next move then the move is stored as an attack and the while loop is broken 
                if (start_x + direction[z][0]) == opponent[b][1] and (start_y + direction[z][1]) == opponent[b][2]:
                    moveable_tiles.append([(start_x + direction[z][0]), (start_y + direction[z][1]), True, b])
                    cont = False
##          If while loop has not been broken then the move is added to the valid moves list and the variables change to that co-ordinate so that on the next loop the next tile in that direction is accessed
            if cont == True:
                moveable_tiles.append([(start_x + direction[z][0]), (start_y + direction[z][1]), False, None])
                start_x += direction[z][0]
                start_y += direction[z][1]

## Defines what happens when a pawn reaches the end of the board
def pawn_change(selected_piece, pieces):
##  initiates small game loop
    change = False
    while change == False:
##      stores position of mouse
        mouse_hover = pygame.mouse.get_pos()
##      Determines if mouse is hovering over the location of a button, if it is a lighter colour is provided to indicate the button is interactive  
        if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 100 and mouse_hover[1] <= 200:
            pygame.draw.rect(gamedisplay, button_2, (900, 100, 200, 100))
        else:
            pygame.draw.rect(gamedisplay, button_1, (900, 100, 200, 100))

        if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 300 and mouse_hover[1] <= 400:
            pygame.draw.rect(gamedisplay, button_2, (900, 300, 200, 100))
        else:
            pygame.draw.rect(gamedisplay, button_1, (900, 300, 200, 100))

        if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 500 and mouse_hover[1] <= 600:
            pygame.draw.rect(gamedisplay, button_2, (900, 500, 200, 100))
        else:
            pygame.draw.rect(gamedisplay, button_1, (900, 500, 200, 100))

        if mouse_hover[0] >= 900 and mouse_hover[0] <= 1100 and mouse_hover[1] >= 700 and mouse_hover[1] <= 800:
            pygame.draw.rect(gamedisplay, button_2, (900, 700, 200, 100))
        else:
            pygame.draw.rect(gamedisplay, button_1, (900, 700, 200, 100))

##      Displays text ontop of the buttons
        gamedisplay.blit(queen_text, (960, 140))
        gamedisplay.blit(bishop_text, (960, 340))
        gamedisplay.blit(castle_text, (960, 540))
        gamedisplay.blit(knight_text, (960, 740))

##      Updates display with new buttons
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
##              Records the mouses position on screen and stores x and y values in seperate variables 
                mouse_position = pygame.mouse.get_pos()
##              If the mouse position is the same as the location of a button, the pawn is changed based on which button is pressed and the loop broken 
                if mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 100 and mouse_position[1] <= 200:
                    pieces[selected_piece][0] = "Q"
                    change = True
                elif mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 300 and mouse_position[1] <= 400:
                    pieces[selected_piece][0] = "B"
                    change = True
                elif mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 500 and mouse_position[1] <= 600:
                    pieces[selected_piece][0] = "C"
                    change = True
                elif  mouse_position[0] >= 900 and  mouse_position[0] <= 1100 and  mouse_position[1] >= 700 and  mouse_position[1] <= 800:
                    pieces[selected_piece][0] = "Kn"
                    change = True
    return pieces
        

                    
## If a piece has been selected by the player then all the tiles it can move to will be displayed by this function 
def highlights(moveable_tiles):
##  Loops through all the stored tiles the piece can move to  
    for n in range(0, len(moveable_tiles)):
##      Decides which colour to display on tile based on if the oponents piece is there 
        if moveable_tiles[n][2] == False:
##          Displays a blue highlight if no piece is there 
            gamedisplay.blit(blue_highlight, (moveable_tiles[n][0], moveable_tiles[n][1]))
        elif moveable_tiles[n][2] == True:
##          Displays a red highlight if a piece is there
            gamedisplay.blit(red_highlight, (moveable_tiles[n][0], moveable_tiles[n][1]))   

## Lists are used to store the pieces each player has aswell as their location and for certain pieces whether they have been moved before or not       
black_pieces = [["K", 300, 0, False], ["Q", 400, 0], ["C", 0, 0, False], ["C", 700, 0, False], ["B", 200, 0], ["B", 500, 0], ["Kn", 100, 0], ["Kn", 600, 0], ["P", 0, 100, False],
                ["P", 100, 100, False], ["P", 200, 100, False], ["P", 300, 100, False], ["P", 400, 100, False], ["P", 500, 100, False], ["P", 600, 100, False],
                ["P", 700, 100, False]]
white_pieces = [["K", 300, 700, False], ["Q", 400, 700], ["C", 0, 700, False], ["C", 700, 700, False], ["B", 200, 700], ["B", 500, 700], ["Kn", 100, 700], ["Kn", 600, 700], ["P", 0, 600, False],
                ["P", 100, 600, False], ["P", 200, 600, False], ["P", 300, 600, False], ["P", 400, 600, False], ["P", 500, 600, False], ["P", 600, 600, False],
                ["P", 700, 600, False]]

## Stores how each piece can move
movement = {
    "WP" : [[0, -100], [-100, -100], [100, -100]],
    "BP" : [[0, 100], [-100, 100], [100, 100]],
    "Kn" : [[200, 100], [200, -100], [100, 200], [-100, 200], [-200, -100], [-200, 100], [-100, -200], [100, -200]],
    "K" : [[0, 100], [100, 100], [100, 0], [100, -100], [0, -100], [-100, -100], [-100, 0], [-100, 100]],
    "C" : [[0, 100], [0, -100], [100, 0], [-100, 0]],
    "B" : [[100, 100], [100, -100], [-100, -100], [-100, 100]],
    "Q" : [[0, 100], [0, -100], [100, 0], [-100, 0], [100, 100], [100, -100], [-100, -100], [-100, 100]],
    }

## Variables are set before game starts:
## Sets the exit condition to False before game starts
finish = False
## Boolean is used to define whos turn it is. Here it sets white to go first as in traditional chess
white_turn = True
## Defines the boolean which is used to decide what section of the turn function should run
piece_selected = False
## Defines the list to store where a piece can move if selected
moveable_tiles = []
## Defines the variable used to store the index number of a selected piece 
selected_piece = None
## Sets win condition to False before game starts
checkmate = False


## Main game loop. Only exited if win condition is met
while not finish:
##  Loops through all events that have occured in the pygame window
    for event in pygame.event.get():
##      Defines what happenes is the close button is pressed 
        if event.type == pygame.QUIT:
##          Sets win condition to true so program can close
            finish = True
##      Defines what happens if the mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONUP:
##          Records the mouses position on screen and stores x and y values in seperate variables while rounding them down to the neares 100
            mouse_position = pygame.mouse.get_pos()
            mouse_position_x = int((mouse_position[0] / 100.0)) * 100
            mouse_position_y = int((mouse_position[1] / 100.0)) * 100
##          Checks if any buttons have been pressed by checking if the mouse co-ordinates are the same as the buttons, if they are the corresponding function is run
            if mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 100 and mouse_position[1] <= 200:
                white_pieces, black_pieces, white_turn = load(white_pieces, black_pieces, white_turn)
            elif mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 300 and mouse_position[1] <= 400:
                save(white_pieces, black_pieces, white_turn)
            elif mouse_position[0] >= 900 and mouse_position[0] <= 1100 and mouse_position[1] >= 500 and mouse_position[1] <= 600:
                finish = True
            elif  mouse_position[0] >= 900 and  mouse_position[0] <= 1100 and  mouse_position[1] >= 700 and  mouse_position[1] <= 800:
                white_pieces, black_pieces, white_turn, checkmate = reset(white_pieces, black_pieces, white_turn, checkmate)
##          Based on the boolean value which determines whose turn it is the 'turn' function is called with the different parameters passed through
            elif white_turn == True:
                white_turn, piece_selected, selected_piece, checkmate = turn(white_pieces, black_pieces, moveable_tiles, mouse_position_x, mouse_position_y, white_turn, piece_selected, selected_piece, checkmate)
            elif white_turn == False:
                white_turn, piece_selected, selected_piece, checkmate = turn(black_pieces, white_pieces, moveable_tiles, mouse_position_x, mouse_position_y, white_turn, piece_selected, selected_piece, checkmate)

    
## Fills the background with he white colour defined above
    gamedisplay.fill(white)
##  If the win condition is met the winner is displayed
    winner = not white_turn
    if checkmate == True:
        if winner == True:
            gamedisplay.blit(white_win_text, (920, 40))
        elif winner == False:
            gamedisplay.blit(black_win_text, (920, 40))
##  Calls the function which draws the basic 8x8 board of chess
    board()
    buttons()
##  Calls the function that displays where selected piece can move
    highlights(moveable_tiles)
##  Calls the function which draws chess pieces onto board, passing the parameters for the white pieces
    draw_pieces(white_pieces, white_king, white_queen, white_castle, white_bishop, white_knight, white_pawn)
##  Calls the function which draws chess pieces onto board, passing the parameters for the black pieces
    draw_pieces(black_pieces, black_king, black_queen, black_castle, black_bishop, black_knight, black_pawn)
##  Updates the pygame display
    pygame.display.update()



## Closes the program
pygame.quit()
quit()
