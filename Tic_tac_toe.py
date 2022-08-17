# Tic Tac Toe - 11.08.2022

import random as rnd
import sys
import turtle
import time

TABLE_HIGH = 600
X = -300
Y = 300
SPACE = TABLE_HIGH / 3

def create_game_basics()-> None:
    table.setup(TABLE_HIGH,TABLE_HIGH)
    table.title('TIC TAC TOE')
    table.bgcolor('blue')

    symbols.color('white')
    symbols.speed(0)
    symbols.pensize(7)
    symbols.hideturtle()


def draw_lines(symbols)->None:
    for a in [1,2]:
        symbols.penup()
        symbols.goto(X + a*SPACE, Y)
        symbols.pendown()
        symbols.goto(X + a*SPACE, -Y)

        symbols.penup()
        symbols.goto(X, Y -a*SPACE)
        symbols.pendown()
        symbols.goto(-X, Y -a*SPACE)
    

def check_winner(board:list)->None:
    
    # diagonally
    if board[0][0] == board[1][1] == board[2][2]: 
        return board[2][2]
    elif board[0][2] == board[1][1] == board[2][0]: 
        return board[2][0]

    # in a row
    for w in range(3): 
        if board[w][0] == board[w][1] == board[w][2]: 
            return board[w][0]
        
    # in a column
    for k in range(2):
        if board[0][k] == board[1][k] == board[2][k]: 
            return board[0][k]


def check_draw(board:list)->bool:
    empty = [board[w][k] for w in range(3) for k in range(3) if board[w][k] == None and check_winner(board) == None]
    if empty == []:
        return True


def draw_symbols(col:int, row:int)->None:
    col_środek = (col*SPACE + SPACE/2) - TABLE_HIGH/2
    row_środek = (-row*SPACE - SPACE/2) + TABLE_HIGH/2

    symbols.penup()
    symbols.goto(col_środek-25, row_środek-25)

    if round == 'x': 
        symbols.write('X', font=('Arial',50))
    else: 
        symbols.write('O', font=('Arial',50))


def new_round(col:int, row:int, round:str)->str:
    board[row][col] = round

    if round == 'o': 
        round = 'x'
    else: 
        round = 'o'

    return round


def print_result()->None:
    if check_winner(board) != None:
        symbols.penup()
        symbols.goto(-150,0)

        time.sleep(1)

        symbols.clear()
        symbols.write(" Wygrały " + check_winner(board), font=("Arial",50))

        time.sleep(3)
        sys.exit(1)
    else:
        if check_draw(board):
            symbols.penup()
            symbols.goto(-100,0)

            time.sleep(1)
            
            symbols.clear()
            symbols.write("REMIS", font=("Arial",50))

            time.sleep(3)
            sys.exit(2)


def click(x,y):
    global round

    col = 0
    row = 0

    if x < X + SPACE: 
        col = 0
    elif x > X + 2*SPACE: 
        col = 2
    else: 
        col = 1

    if y < Y - 2*SPACE: 
        row = 2
    elif y > Y - SPACE: 
        row = 0
    else: 
        row = 1


    if board[row][col] != None: 
        return

    draw_symbols(col, row)

    round = new_round(col, row, round)
    
    print_result()
        

if __name__ == '__main__':
    table = turtle.Screen()
    symbols = turtle.Turtle()

    board = [[None,None,None],
            [None,None,None],
            [None,None,None]]

    round = rnd.choice(['x','o'])
    
    create_game_basics()
    
    draw_lines(symbols)
    
    table.onclick(click)
    table.listen()
    table.mainloop()