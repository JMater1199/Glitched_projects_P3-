import turtle
import random

# I am tring to add some notes for the first time :)

screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Connect 4")
turtle.speed(0)
turtle.ht()
screen.tracer(0,0) # -- Immediate draw and update
t = turtle.Turtle()
t.up()

# make a rectangle def for future

def draw_rectangle():
  t.goto(-350, -100)
  t.fillcolor('skyblue')
  t.pendown()
  t.begin_fill()
  t.goto(-350, 500)
  t.goto(350, 500)
  t.goto(350, -100)
  t.goto(-350, -100)
  t.end_fill()
  t.up()
# 6 rows and 7 columns

Nr = 6
Nc = 7

def draw_circle(x, y, r, fillcolor):

  # make a circle so that we can actually make the holes in connet 4
  #also it is customizably using the x and y axies

  t.goto(x, y)
  t.setheading(-90)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(r)
  t.end_fill()

board = []

nR = 6
nC = 7

board = [[0 for i in range(nC)] for j in range(nR)]

def draw_board():
  draw_rectangle()

  for kk in range(Nr):
    for jj in range(Nc):
      if board[kk][jj] == 0:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'white')
      if board[kk][jj] == 1:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'red')
      if board[kk][jj] == 2:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'blue')

  screen.update()

def all_same(cells, value):

  #Return true if all values of the list 
  #cells are equal to value

  alle = True
  
  for cell in cells: 
    if cell != value:
      alle = False
      break

  return alle
  
def checkHorizontalWinner(value):
  # check for enny winns horizontaly
  win = False
  for jj in range(nR):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj][kk+cnt])
      if all_same(cells, value):
        win = True
        return win

  return win

def checkVerticalWinner(value):
  win = False
  #same as lest coment but vertical
  for jj in range(3):
    for kk in range(nC):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk])
      if all_same(cells, value):
        win = True
        return win

  return win

def checkDiagonalOneWinner(value):

  win = False
  #same again but sloping upwards
  for jj in range(3,nR,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj-cnt][kk+cnt])
      if all_same(cells, value):
        win = True
        return win

  return win

def checkDiagonalTwoWinner(value):

  win = False
  #last one for sloping downwards
  for jj in range(0,3,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk+cnt])
      if all_same(cells, value):
        win = True
        return win

  return win

def checkwinner(value):
  
  win = checkHorizontalWinner(value)
  if not win:
    win = checkVerticalWinner(value)
    if not win:
      win = checkDiagonalOneWinner(value)
      if not win:
        win = checkDiagonalTwoWinner(value)
        
  return win

def lowest_row(col):
  
  r = -1
  for kk in range(Nr-1, -1, -1):
    if board[kk][col] == 0:
      r = kk
      break
      
  return r

def play(x, y):
#this go variable is Game over
  global turn, go
  if go:
    return
  
  col = int((x + 350)//100) 
  
  if col < 0: 
    col = 0
  if col > Nc-1:
    col = Nc - 1

  avail_cols = find_open_cols()

  if col in avail_cols:
    available_row = lowest_row(col)
    board[available_row][col] = 1
  
    draw_board()
    # Check if somone has win and wether the play plays again
    if checkwinner(1):
      go = True
      print('Player Wins')
    else:
      turn = 2
  
  if turn == 2:
    playc()

def find_open_cols():
  open_cols = [m for m in range(Nc)]
  full_cols = []
 
  for col in open_cols:
    if lowest_row(col) == -1:
      full_cols.append(col)

  for col in full_cols:
    open_cols.remove(col)

  return open_cols

def display_board():
  for kk in range(nR):
    print(board[kk])

def playc():
  global turn, go
  
  cols_avail = find_open_cols()
  
  if len(cols_avail) > 0:
    col = random.choice(cols_avail)
    available_row = lowest_row(col)
    board[available_row][col] = 2
    draw_board()

    if checkwinner(2):
      go = True
      print('Computer Wins')
    else:
      turn = 1
  else:
    turn = 1

gameOver = False   
turn = 1
go = False

draw_board()
screen.onclick(play)