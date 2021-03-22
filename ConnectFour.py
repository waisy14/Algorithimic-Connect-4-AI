from copy import deepcopy
import random
random.seed(108)
import pygame

gamewinrow1 = 0
gamewinrow2 = 0


gamewincol1 = 1
gamewincol2 = 1

def print_board(board):
    print()
    print(' ', end='')
    for x in range(1, len(board) + 1):
        print(' %s  ' % x, end='')
    print()

    print('+---+' + ('---+' * (len(board) - 1)))

    for y in range(len(board[0])):
        print('|   |' + ('   |' * (len(board) - 1)))

        print('|', end='')
        for x in range(len(board)):
            print(' %s |' % board[x][y], end='')
        print()

        print('|   |' + ('   |' * (len(board) - 1)))

        print('+---+' + ('---+' * (len(board) - 1)))

def select_space(board, column, player):
    if not move_is_valid(board, column):
        return False
    if player != "X" and player != "O":
        return False
    for y in range(len(board[0])-1, -1, -1):
        if board[column-1][y] == ' ':
            board[column-1][y] = player
            global pycol 
            global pyrow
            pycol = column-1
            pyrow = y
            
            return True
    return False

def board_is_full(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == ' ':
                return False
    return True

def move_is_valid(board, move):
    if move < 1 or move > (len(board)):
        return False

    if board[move-1][0] != ' ':
        return False

    return True

def available_moves(board):
    moves = []
    for i in range(1, len(board)+1):
        if move_is_valid(board, i):
            moves.append(i)
    return moves

def has_won(board, symbol):
    # check horizontal spaces
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                gamewincol1 = x
                gamewinrow1 = y
                gamewincol2 = x+3
                gamewinrow2 = y
                return True

    # check vertical spaces
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                gamewincol1 = x
                gamewinrow1 = y
                gamewincol2 = x
                gamewinrow2 = y+3
                return True

    # check / diagonal spaces
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                gamewincol1 = x
                gamewinrow1 = y
                gamewincol2 = x+3
                gamewinrow2 = y-3
                return True

    # check \ diagonal spaces
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol:
                gamewincol1 = x
                gamewinrow1 = y
                gamewincol2 = x+3
                gamewinrow2 = y+3
                return True

    return False


def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def codecademy_evaluate_board(board):
    if has_won(board, "X"):
      return float("Inf")
    elif has_won(board, "O"):
      return -float("Inf")
    else:
      x_streaks = count_streaks(board, "X")
      o_streaks = count_streaks(board, "O")
      return x_streaks - o_streaks

def count_streaks(board, symbol):
    count = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] != symbol:
                continue
            # right
            if col < len(board) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #left
            if col > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-right
            if col < len(board) - 3 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-right
            if col < len(board) - 3 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-left
            if col > 2 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down
            num_in_streak = 0
            if row < len(board[0]) - 3:
                for i in range(4):
                    if row + i < len(board[0]):
                        if board[col][row + i] == symbol:
                            num_in_streak += 1
                        else:
                            break
            for i in range(4):
                if row - i > 0:
                    if board[col][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col][row - i] == " ":
                        break
                    else:
                        num_in_streak == 0
            if row < 3:
                if num_in_streak + row < 4:
                    num_in_streak = 0
            count += num_in_streak
    return count

def minimax(input_board, is_maximizing, depth, alpha, beta, eval_function):
  if game_is_over(input_board) or depth == 0:
        return [eval_function(input_board), ""]
  if is_maximizing:
    best_value = -float("Inf")
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, "X")
      hypothetical_value = minimax(new_board, False, depth - 1, alpha, beta, eval_function)[0]
      if hypothetical_value > best_value:
        best_value = hypothetical_value
        best_move = move
      alpha = max(alpha, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]
  else:
    best_value = float("Inf")
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, "O")
      hypothetical_value = minimax(new_board, True, depth - 1, alpha, beta, eval_function)[0]
      if hypothetical_value < best_value:
        best_value = hypothetical_value
        best_move = move
      beta = min(beta, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]

def make_board():
    new_game = []
    for x in range(7):
        new_game.append([' '] * 6)
    return new_game

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True,4 , -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), the_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


def random_eval(board): 
  return random.randint(-100, 100)

def my_evaluate_board(board):
  if has_won(board,'X'):
    return float('Inf')
  elif has_won(board,'O'):
    return -float('Inf')
  x_two_streak = 0
  o_two_streak = 0
  x_three_streak = 0
  o_three_streak = 0


#Rows
  for col in range(len(board)- 1):
    for row in range(len(board[0])):
      if board[col][row] == 'X' and board[col + 1][row] == 'X':
        x_two_streak += 1
      if board[col][row] == 'O' and board[col + 1][row] == 'O': 
        o_two_streak += 1
  for col in range(len(board)- 2):
    for row in range(len(board[0])):
      if board[col][row] == 'X' and board[col + 1][row] == 'X' and board[col+ 2][row] == 'X' :
        x_three_streak += 1
      if board[col][row] == 'O' and board[col + 1][row] == 'O' and board[col + 2][row] == 'O': 
        o_three_streak += 1

      
    #Columns

  for col in range(len(board)):
    for row in range(len(board[0]) - 1 ):
      if board[col][row] == 'X' and board[col][row + 1] == 'X':
        x_two_streak += 1
      if board[col][row] == 'O' and board[col][row + 1] == 'O': 
        o_two_streak += 1

  for col in range(len(board)):
    for row in range(len(board[0]) - 2 ):
      if board[col][row] == 'X' and board[col][row + 1] == 'X' and board[col][row + 2] == 'X':
        x_three_streak += 1
      if board[col][row] == 'O' and board[col][row + 1] == 'O' and board[col][row + 2] == 'O': 
        o_three_streak += 1


  #Diagonals 
  for col in range(len(board) - 1):
    for row in range(len(board[0]) - 1 ):
      if board[col][row] == 'X' and board[col + 1][row + 1] == 'X' :
        x_three_streak += 1
      if board[col][row] == 'O' and board[col + 1][row + 1] == 'O' : 
        o_two_streak += 1


  for col in range(len(board)- 2):
    for row in range(len(board[0]) - 2 ):
      if board[col][row] == 'X' and board[col + 1][row + 1] == 'X' and board[col + 2][row + 2] == 'X':
        x_three_streak += 1
      if board[col][row] == 'O' and board[col + 1][row + 1] == 'O' and board[col + 2][row + 2] == 'O': 
        o_three_streak += 1


  x_center_control = 0
  o_center_control = 0 

  for square in board[3]:
    if square == "X":
      x_center_control += 1
    elif square == "O":
        o_center_control += 1


  final_score_x = 0
  final_score_o = 0 
  final_score_x = x_two_streak + x_three_streak ** 2
  final_score_o = o_two_streak + o_three_streak ** 2
  return final_score_x - final_score_o + (x_center_control - o_center_control)  * 10

































def the_evaluate_board(board):
  if has_won(board, "X"):
    return float("Inf")
  elif has_won(board, "O"):
    return -float("Inf")
  x_two_streak = 0
  o_two_streak = 0
  x_three_streak = 0
  o_three_streak = 0
  x_center_control = 0
  o_center_control = 0

  #2 streaks
  #horizontally
  for col in range(len(board) - 1):
    for row in range(len(board[0])):
      if board[col][row] == "X" and board[col + 1][row] == "X":
        x_two_streak += 1
  for col in range(len(board) - 1):
    for row in range(len(board[0])):
      if board[col][row] == "O" and board[col + 1][row] == "O":
        o_two_streak += 1
    #left diagonally
  for col in range(len(board) - 1):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "X" and board[col + 1][row - 1] == "X":
        x_two_streak += 1
  for col in range(len(board) - 1):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "O" and board[col + 1][row - 1] == "O":
        o_two_streak += 1
  #right diagonally
  for col in range(len(board) - 1):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "X" and board[col + 1][row + 1] == "X":
        x_two_streak += 1
  for col in range(len(board) - 1):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "O" and board[col + 1][row + 1] == "O":
        o_two_streak += 1
  #vertically
  for col in range(len(board)):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "X" and board[col][row + 1] == "X":
        x_two_streak += 1
  for col in range(len(board)):
    for row in range(len(board[0]) - 1):
      if board[col][row] == "O" and board[col][row + 1] == "O":
        o_two_streak += 1

  #3 Streaks

  for col in range(len(board) - 2):
    for row in range(len(board[0])):
      if board[col][row] == "X" and board[col + 1][row] == "X" and board[col + 2][row] == "X":
        x_three_streak += 1
  for col in range(len(board) - 2):
    for row in range(len(board[0])):
      if board[col][row] == "O" and board[col + 1][row] == "O" and board[col + 2][row] == "O":
        o_three_streak += 1
    #left diagonally
  for col in range(len(board) - 2):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "X" and board[col + 1][row - 1] == "X" and board[col + 2][row - 2] == "X":
        x_three_streak += 1
  for col in range(len(board) - 2):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "O" and board[col + 1][row - 1] == "O" and board[col + 2][row - 2] == "O":
        o_three_streak += 1
  #right diagonally
  for col in range(len(board) - 2):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "X" and board[col + 1][row + 1] == "X" and board[col + 2][row + 2] == "X":
        x_three_streak += 1
  for col in range(len(board) - 2):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "O" and board[col + 1][row + 1] == "O" and board[col + 2][row + 2] == "O":
        o_three_streak += 1
  #vertically
  for col in range(len(board)):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "X" and board[col][row + 1] == "X" and board[col][row + 2] == "X":
        x_three_streak += 1
  for col in range(len(board)):
    for row in range(len(board[0]) - 2):
      if board[col][row] == "O" and board[col][row + 1] == "O" and board[col][row + 2]:
        o_three_streak += 1

  #center control
  for square in board[3]:
    if square == "X":
      x_center_control += 1
    elif square == "O":
      o_center_control += 1


  return (x_center_control - o_center_control) * 5 + (x_two_streak - o_two_streak) + 2 * (x_three_streak - o_three_streak) 













pygame.init()

pygame.display.set_caption("Connect 4")

screen = pygame.display.set_mode((640, 600))



boardImg = pygame.image.load("Connect4Board.png")

redCircleImg = pygame.image.load("RedCircle.png")
redCircleImg = pygame.transform.scale(redCircleImg, (71, 71))

yellowCircleImg = pygame.image.load("YellowCircle.jpg")
yellowCircleImg = pygame.transform.scale(yellowCircleImg, (75, 75))

upArrowImg = pygame.image.load("Arrow.png")
upArrowImg = pygame.transform.scale(upArrowImg, (50, 50))

downArrowImg = pygame.image.load("Arrow.png")
downArrowImg = pygame.transform.flip(downArrowImg, False, True)
downArrowImg = pygame.transform.scale(downArrowImg, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 64)
smallFont = pygame.font.Font('freesansbold.ttf', 32)
mediumFont = pygame.font.Font('freesansbold.ttf', 48)
yellowFont = pygame.font.Font('freesansbold.ttf', 40)
aiFont = pygame.font.Font('freesansbold.ttf', 35)

Connectfour = font.render("Connect 4", True, (0, 0, 0))
redButtonText = mediumFont.render("Red", True, (0, 0, 0))
yellowButtonText = yellowFont.render("Yellow", True, (0, 0, 0))
aiButtonText = aiFont.render("Ai vs Ai", True, (0, 0, 0))
playAs = mediumFont.render("Play As", True, (0, 0, 0))
speedText = yellowFont.render("Drop Speed", True, (0, 0, 0))
playText = yellowFont.render("PLAY", True, (0, 0, 0))

boardCoords = [
[(14, 125), (104, 125), (194, 125), (284, 125), (374, 125), (464, 125), (554, 125)],
[(14, 205), (104, 205), (194, 205), (284, 205), (374, 205), (464, 205), (554, 205)],
[(14, 285), (104, 285), (194, 285), (284, 285), (374, 285), (464, 285), (554, 285)],
[(14, 365), (104, 365), (194, 365), (284, 365), (374, 365), (464, 365), (554, 365)],
[(14, 445), (104, 445), (194, 445), (284, 445), (374, 445), (464, 445), (554, 445)],
[(14, 525), (104, 525), (194, 525), (284, 525), (374, 525), (464, 525), (554, 525)],

]

redBoardCoordsFilled = []
yellowBoardCoordsFilled = []
dropped_pieces = []
 








def playerasyellow(ai, depth, speed):
    redSide = False
    yellowSide = True
    running = True
    my_board = make_board()
    dropY = 45
    gameIsOver = False
    while running:

        #background colour
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yellowSide == True:
                        moves = available_moves(my_board)
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if mouseX <= 96:
                            choice = 1
                        elif mouseX >= 97 and mouseX <= 186:
                            choice = 2
                        elif mouseX >= 187 and mouseX <= 274:
                            choice = 3
                        elif mouseX >= 275 and mouseX <= 366:
                            choice = 4
                        elif mouseX >= 367 and mouseX <= 454:
                            choice = 5
                        elif mouseX >= 455 and mouseX <= 546:
                            choice = 6
                        elif mouseX >= 547:
                            choice = 7   
                        try:
                            move = int(choice)
                        except ValueError:
                            continue
                        if move in moves:
                            good_move = True
                            select_space(my_board, choice, "X")
                            dropped_pieces.append(("X", boardCoords[pyrow][pycol]))
                            yellowSide = False
                            
            except:
                running = False


        

        #top circle thingy
        
        if redSide:
            result = minimax(my_board, False, depth, -float("Inf"), float("Inf"), ai)
            select_space(my_board, result[1], "O")

            dropped_pieces.append(("O", boardCoords[pyrow][pycol]))

           




        if yellowSide == True:
            moves = available_moves(my_board)
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX <= 96:
                screen.blit(yellowCircleImg, (14, 45))
            elif mouseX >= 97 and mouseX <= 186:
                screen.blit(yellowCircleImg, (104, 45))
            elif mouseX >= 187 and mouseX <= 274:
                screen.blit(yellowCircleImg, (194, 45))
            elif mouseX >= 275 and mouseX <= 366:
                screen.blit(yellowCircleImg, (284, 45))
            elif mouseX >= 367 and mouseX <= 454:
                screen.blit(yellowCircleImg, (374, 45))
            elif mouseX >= 455 and mouseX <= 546:
                screen.blit(yellowCircleImg, (464, 45))
            elif mouseX >= 456:
                screen.blit(yellowCircleImg, (554, 45))


    

        
        
        for yellowcircle in yellowBoardCoordsFilled:
            screen.blit(yellowCircleImg, yellowcircle)
        for redcircle in redBoardCoordsFilled:
            screen.blit(redCircleImg, redcircle)

        if len(dropped_pieces) >= 1:
            if dropped_pieces[0][0] == "O":
                redSide = False
                screen.blit(redCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    redBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    yellowSide = True
                    

            elif dropped_pieces[0][0] == "X":
                screen.blit(yellowCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    yellowBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    redSide = True
                    



            

        screen.blit(boardImg, (0, 120))

        if gameIsOver:

            winrow1, wincol1 = boardCoords[gamewinrow1][gamewincol1]
            winrow2, wincol2 = boardCoords[gamewinrow2][gamewincol2]
            winrow1 += 35
            winrow2 += 35
            wincol1 += 45
            wincol2 += 45

            yellowSide = False
            redSide = False
            if has_won(my_board, "X"):
                yellowwon = font.render("YELLOW WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(yellowwon, (100, 50))
            elif has_won(my_board, "O"):
                redwon = font.render("RED WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(redwon, (150, 50))
            elif len(available_moves(my_board)) == 0:
                tietext = font.render("ITS A TIE", True, (0, 0, 0))
                screen.blit(tietext, (190, 50))
            #click_anywhere_to_exit = smallFont.render("Click anywhere to exit", True, (0, 0, 0))
            #screen.blit(click_anywhere_to_exit, (150, 400))

        
        pygame.display.update()


def aigame(ai, ai2, depth, speed):
    redSide = False
    yellowSide = True
    running = True
    my_board = make_board()
    dropY = 45
    gameIsOver = False
    while running:
        #background colour
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        if yellowSide:
            result = minimax(my_board, True, depth, -float("Inf"), float("Inf"), ai2)
            select_space(my_board, result[1], "X")

            dropped_pieces.append(("X", boardCoords[pyrow][pycol]))

        

        #top circle thingy
        
        if redSide:
            result = minimax(my_board, False, depth, -float("Inf"), float("Inf"), ai)
            select_space(my_board, result[1], "O")

            dropped_pieces.append(("O", boardCoords[pyrow][pycol]))

           

        
        
        for yellowcircle in yellowBoardCoordsFilled:
            screen.blit(yellowCircleImg, yellowcircle)
        for redcircle in redBoardCoordsFilled:
            screen.blit(redCircleImg, redcircle)

        if len(dropped_pieces) >= 1:
            if dropped_pieces[0][0] == "O":
                redSide = False
                screen.blit(redCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    redBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    yellowSide = True
                    

            elif dropped_pieces[0][0] == "X":
                yellowSide = False
                screen.blit(yellowCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    yellowBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    redSide = True
                    



            

        screen.blit(boardImg, (0, 120))

        if gameIsOver:

            winrow1, wincol1 = boardCoords[gamewinrow1][gamewincol1]
            winrow2, wincol2 = boardCoords[gamewinrow2][gamewincol2]
            winrow1 += 35
            winrow2 += 35
            wincol1 += 45
            wincol2 += 45

            yellowSide = False
            redSide = False
            if has_won(my_board, "X"):
                yellowwon = font.render("YELLOW WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(yellowwon, (100, 50))
            elif has_won(my_board, "O"):
                redwon = font.render("RED WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(redwon, (150, 50))
            elif len(available_moves(my_board)) == 0:
                tietext = font.render("ITS A TIE", True, (0, 0, 0))
                screen.blit(tietext, (190, 50))
            #click_anywhere_to_exit = smallFont.render("Click anywhere to exit", True, (0, 0, 0))
            #screen.blit(click_anywhere_to_exit, (150, 400))

        
        pygame.display.update()



def playerasred(ai, depth, speed):
    redSide = False
    yellowSide = True
    running = True
    my_board = make_board()
    dropY = 45
    gameIsOver = False
    while running:
        #background colour
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if redSide == True:
                        moves = available_moves(my_board)
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if mouseX <= 96:
                            choice = 1
                        elif mouseX >= 97 and mouseX <= 186:
                            choice = 2
                        elif mouseX >= 187 and mouseX <= 274:
                            choice = 3
                        elif mouseX >= 275 and mouseX <= 366:
                            choice = 4
                        elif mouseX >= 367 and mouseX <= 454:
                            choice = 5
                        elif mouseX >= 455 and mouseX <= 546:
                            choice = 6
                        elif mouseX >= 547:
                            choice = 7   
                        try:
                            move = int(choice)
                        except ValueError:
                            continue
                        if move in moves:
                            good_move = True
                            select_space(my_board, choice, "O")
                            dropped_pieces.append(("O", boardCoords[pyrow][pycol]))
                            redSide = False
            except:
                running = False


        

        #top circle thingy
        
        if yellowSide:
            result = minimax(my_board, True, depth, -float("Inf"), float("Inf"), ai)
            select_space(my_board, result[1], "X")

            dropped_pieces.append(("X", boardCoords[pyrow][pycol]))

           




        if redSide == True:
            moves = available_moves(my_board)
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX <= 96:
                screen.blit(redCircleImg, (14, 45))
            elif mouseX >= 97 and mouseX <= 186:
                screen.blit(redCircleImg, (104, 45))
            elif mouseX >= 187 and mouseX <= 274:
                screen.blit(redCircleImg, (194, 45))
            elif mouseX >= 275 and mouseX <= 366:
                screen.blit(redCircleImg, (284, 45))
            elif mouseX >= 367 and mouseX <= 454:
                screen.blit(redCircleImg, (374, 45))
            elif mouseX >= 455 and mouseX <= 546:
                screen.blit(redCircleImg, (464, 45))
            elif mouseX >= 456:
                screen.blit(redCircleImg, (554, 45))


    

        
        
        for yellowcircle in yellowBoardCoordsFilled:
            screen.blit(yellowCircleImg, yellowcircle)
        for redcircle in redBoardCoordsFilled:
            screen.blit(redCircleImg, redcircle)

        if len(dropped_pieces) >= 1:
            if dropped_pieces[0][0] == "O":
                screen.blit(redCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                redSide = False
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    redBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    yellowSide = True
                    

            elif dropped_pieces[0][0] == "X":
                screen.blit(yellowCircleImg, (dropped_pieces[0][1][0], dropY))
                dropY += speed
                yellowSide = False
                if dropped_pieces[0][1] == (dropped_pieces[0][1][0], dropY):
                    yellowBoardCoordsFilled.append(dropped_pieces[0][1])
                    dropped_pieces.pop(0)
                    dropY = 45
                    if game_is_over(my_board):
                        gameIsOver = True
                    redSide = True
                    



            

        screen.blit(boardImg, (0, 120))

        if gameIsOver:

            winrow1, wincol1 = boardCoords[gamewinrow1][gamewincol1]
            winrow2, wincol2 = boardCoords[gamewinrow2][gamewincol2]
            winrow1 += 35
            winrow2 += 35
            wincol1 += 45
            wincol2 += 45

            yellowSide = False
            redSide = False
            if has_won(my_board, "X"):
                yellowwon = font.render("YELLOW WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(yellowwon, (100, 50))
            elif has_won(my_board, "O"):
                redwon = font.render("RED WINS", True, (0, 0, 0))
                pygame.draw.line(screen, (0, 0, 0), (winrow1, wincol1), (winrow2, wincol2), 10)
                screen.blit(redwon, (150, 50))
            elif len(available_moves(my_board)) == 0:
                tietext = font.render("ITS A TIE", True, (0, 0, 0))
                screen.blit(tietext, (190, 50))
            #click_anywhere_to_exit = smallFont.render("Click anywhere to exit", True, (0, 0, 0))
            #screen.blit(click_anywhere_to_exit, (150, 400))

        
        pygame.display.update()

depthText = font.render("Depth", True, (0, 0, 0))

def gameloadingscreen():
    loadingScreen = True
    redButton = False
    yellowButton = False
    aiButton = False
    depthnessNumber = 5
    speedNumber = 5
    depthnessNumberText = font.render(str(depthnessNumber), True, (0, 0, 0))
    speedNumberText = font.render(str(speedNumber), True, (0, 0, 0))
    while loadingScreen:
        screen.fill((255, 255, 255))
        screen.blit(Connectfour, (175, 50))
        screen.blit(playAs, (230, 115))

        pygame.draw.rect(screen, (0,0,0), (50, 175, 150, 75))
        mouseX, mouseY = pygame.mouse.get_pos()
        if redButton:
            pygame.draw.rect(screen, (180, 180, 180), (55, 180, 140, 65))
        elif mouseX < 200 and mouseX > 50 and mouseY > 200 and mouseY < 275:
            pygame.draw.rect(screen, (192, 192, 192), (55, 180, 140, 65))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (55, 180, 140, 65))
        screen.blit(redButtonText, (75, 190))

        pygame.draw.rect(screen, (0,0,0), (250, 175, 150, 75))
        mouseX, mouseY = pygame.mouse.get_pos()
    
        if yellowButton:
            pygame.draw.rect(screen, (180, 180, 180), (255, 180, 140, 65))
        elif mouseX < 350 and mouseX > 250 and mouseY > 200 and mouseY < 275:
            pygame.draw.rect(screen, (192, 192, 192), (255, 180, 140, 65))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (255, 180, 140, 65))
        screen.blit(yellowButtonText, (260, 195))

        pygame.draw.rect(screen, (0,0,0), (450, 175, 150, 75))
        mouseX, mouseY = pygame.mouse.get_pos()
        if aiButton:
            pygame.draw.rect(screen, (180, 180, 180), (455, 180, 140, 65))
        elif mouseX < 600 and mouseX > 450 and mouseY > 200 and mouseY < 275:
            pygame.draw.rect(screen, (192, 192, 192), (455, 180, 140, 65))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (455, 180, 140, 65))
        screen.blit(aiButtonText, (457, 195))

        screen.blit(depthText, (235, 260))

        pygame.draw.rect(screen, (0, 0, 0), (275, 325, 100, 75))
        pygame.draw.rect(screen, (255, 255, 255), (280, 330, 90, 65))
        screen.blit(depthnessNumberText, (305, 340))

    
        pygame.draw.rect(screen, (0, 0, 0), (210, 330, 60, 60))
        if mouseX > 210 and mouseX < 270 and mouseY > 330 and mouseY < 390:
            pygame.draw.rect(screen, (192, 192, 192), (215, 335, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (215, 335, 50, 50))
    
        pygame.draw.rect(screen, (0, 0, 0), (380, 330, 60, 60))
        if mouseX > 380 and mouseX < 440 and mouseY > 330 and mouseY < 390:
            pygame.draw.rect(screen, (192, 192, 192), (385, 335, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (385, 335, 50, 50))
        screen.blit(upArrowImg, (215, 335))
        screen.blit(downArrowImg, (385, 335))


        screen.blit(speedText, (210, 400))

        pygame.draw.rect(screen, (0, 0, 0), (275, 440, 100, 75))
        pygame.draw.rect(screen, (255, 255, 255), (280, 445, 90, 65))
        screen.blit(speedNumberText, (305, 455))

    
        pygame.draw.rect(screen, (0, 0, 0), (210, 445, 60, 60))
        if mouseX > 210 and mouseX < 270 and mouseY > 445 and mouseY < 510:
            pygame.draw.rect(screen, (192, 192, 192), (215, 450, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (215, 450, 50, 50))
    
        pygame.draw.rect(screen, (0, 0, 0), (380, 445, 60, 60))
        if mouseX > 380 and mouseX < 440 and mouseY > 445 and mouseY < 510:
            pygame.draw.rect(screen, (192, 192, 192), (385, 450, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (385, 450, 50, 50))
        screen.blit(upArrowImg, (215, 450))
        screen.blit(downArrowImg, (385, 450))

        pygame.draw.rect(screen, (0, 0, 0), (250, 525, 150, 50))
        if mouseX > 255 and mouseX < 395 and mouseY > 530 and mouseY < 570:
            pygame.draw.rect(screen, (192, 192, 192), (255, 530, 140, 40))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (255, 530, 140, 40))

        screen.blit(playText, (270, 535))


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loadingScreen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseX < 200 and mouseX > 50 and mouseY > 200 and mouseY < 275:
                    redButton = True
                    yellowButton = False
                    aiButton = False
                elif mouseX < 350 and mouseX > 250 and mouseY > 200 and mouseY < 275:
                    redButton = False
                    yellowButton = True
                    aiButton = False
                elif mouseX < 600 and mouseX > 450 and mouseY > 200 and mouseY < 275:
                    redButton = False
                    yellowButton = False
                    aiButton = True
                elif mouseX > 210 and mouseX < 270 and mouseY > 330 and mouseY < 390:
                    if depthnessNumber < 8:
                        depthnessNumber += 1
                        depthnessNumberText = font.render(str(depthnessNumber), True, (0, 0, 0))
                elif mouseX > 380 and mouseX < 440 and mouseY > 330 and mouseY < 390:
                    if depthnessNumber > 1:
                        depthnessNumber -= 1
                        depthnessNumberText = font.render(str(depthnessNumber), True, (0, 0, 0))
                elif mouseX > 210 and mouseX < 270 and mouseY > 445 and mouseY < 505:
                    speedNumber += 1
                    speedNumberText = font.render(str(speedNumber), True, (0, 0, 0))
                elif mouseX > 380 and mouseX < 440 and mouseY > 445 and mouseY < 505:
                    if speedNumber > 1:
                        speedNumber -= 1
                        speedNumberText = font.render(str(speedNumber), True, (0, 0, 0))
                elif mouseX > 255 and mouseX < 395 and mouseY > 530 and mouseY < 570:
                    loadingScreen = False
                    if redButton:
                        loadingScreen = False
                    elif yellowButton:
                        loadingScreen = False
                    elif aiButton:
                        loadingScreen = False

        pygame.display.flip()

    if redButton:
        playerasred(the_evaluate_board, depthnessNumber, speedNumber)
        new_board = make_board()
    elif yellowButton:
        playerasyellow(the_evaluate_board, depthnessNumber, speedNumber)
        new_board = make_board()
    elif aiButton:
        aigame(the_evaluate_board, my_evaluate_board, depthnessNumber, speedNumber)
        new_board = make_board()

    pygame.display.flip()

gameloadingscreen()