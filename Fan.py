from time import sleep
from Mines import Cos, Sin
from UI import Clear

blade = "X"
blank = " "
size = 21
fan = [[blank for i in range(size)] for j in range(size)]
for i in range(size):
    for j in range(size):
        if i==int((size-1)/2) or j==int((size-1)/2):
            fan[i][j] = blade

def Center():
    return int((size-1)/2)

def ShowFan():
    Clear()
    for line in fan:
        print(" ".join(line))

def MoveLeft(x,y):
    fan[y][x-1] = blade
    fan[y][x] = blank

def MoveRight(x, y):
    fan[y][x+1] = blade
    fan[y][x] = blank

def Reset_X():
    global total_right, total_left
    total_left = 0
    total_right = 0

def Sum_X():
    global total_right, total_left
    total_left += 1
    total_right += 1

def MoveDown(x, y):
    try:
        fan[y+1][x] = blade
        fan[y][x] = blank
    except:
        pass

def MoveUp(x, y):
    try:
        fan[y-1][x] = blade
        fan[y][x] = blank
    except:
        pass

def Start():
    Reset_X()
    while True:
        ShowFan()
        move_down = True
        for y in range(size):
            down_moves = 0
            move_right = True
            for x in range(size):
                if fan[y][x] == blade:
                    if y<Center() and y<Center()-total_left:
                        MoveLeft(x,y)
                    elif y>Center() and x>=Center() and y>Center()+total_right and move_right:
                        MoveRight(x,y)
                        move_right = False
                if fan[y][x] == blade:
                    if y>=Center() and x<Center() and move_down:
                        MoveDown(x,y)
                        down_moves += 1
                if down_moves >= 10:
                    move_down = False
        input()
        Sum_X()
Start()
