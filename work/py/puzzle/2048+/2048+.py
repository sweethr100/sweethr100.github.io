import random
import os
import sys

def printMap(data):
    os.system("cls")
    for y in data:
        for x in y:
            sys.stdout.write("\033[44m")
            if x == 0:
                sys.stdout.write("\033[34m")
            print("%3d"%x,end="")
            sys.stdout.write("\033[37m")
            sys.stdout.write("\033[40m")
        print("")

def rotation(data):
    re = []
    for y in range(len(data)):
        tmp = []
        for x in range(len(data[y])):
            tmp.append(data[x][len(data)-y-1])
        re.append(tmp)
    return re

def sumdata(data):
    for y in range(len(data)):
        for x in range(len(data[y])-1):
            if data[y][x] == data[y][x+1]:
                data[y][x]*=2
                data[y][x+1]=0
    return data

def move(data,user):
    if user=="s":
        data = rotation(rotation(rotation(data)))
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(data)
    if user=="w":
        data = rotation(data)
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(rotation(rotation(data)))
    if user=="a":
        data = left(data)
        data = sumdata(data)
        data = left(data)
    if user=="d":
        data = rotation(rotation(data))
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(rotation(data))
    return data

def left(data):
    for z in range(len(data)-1):
        for y in range(len(data)):
            for x in range(len(data[y])-1):
                if data[y][x] == 0:
                    data[y][x] = data[y][x+1]
                    data[y][x+1] = 0
    return data

def push(data):
    pos=[]
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x]==0:
                pos.append([y,x])
    if len(pos) != 0:
        r = random.choice([2,2,2,2,4])
        xy = random.choice(pos)
        data[xy[0]][xy[1]]= r
    return data

def isEnd(data):
    for t in data:
        if 2048 in t:
            return True

    for t in data:
        if 0 in t:
            return False

        for y in range(len(data)):
            for x in range(len(data[y]) - 1):
                if data[y][x] == data[y][x + 1]:
                    return False

        for y in range(len(data)-1):
            for x in range(len(data[y])):
                if data[y][x] == data[y+1][x ]:
                    return False
    return True

def lol(data):
    data.append(data)
    lol(data)

if __name__ == "__main__":
    data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    data=push(push(data))

    while True:
        data = push(data)
        if isEnd(data):
            break
        printMap(data)
        user = input(">:")
        data = move(data, user)