from random import randrange as rand
from math import sin, cos, radians as rad
import os
os.system("cls")

bomb = "B"
size = 10
table = [[0 for i in range(size)] for j in range(size)]

def Cos(angle):
    return round(cos(rad(angle)))

def Sin(angle):
    return round(sin(rad(angle)))

def AddAdjacent(x, y):
    for i in range(0, 360, 45):
        try:
            table[x+Cos(i)][y+Sin(i)] += 1
        except:
            pass

def ShowTable():
    for line in table:
        print(" ".join(map(str, line)))

def GenerateBombs(num):
    while num > 0:
        x, y = rand(size), rand(size)
        if table[x][y] != bomb:
            table[x][y] = bomb
            num -= 1

def PrepareNumbers():
    for i in range(size):
        for j in range(size):
            if table[i][j] == bomb:
                AddAdjacent(i, j)

GenerateBombs(10)
PrepareNumbers()
ShowTable()