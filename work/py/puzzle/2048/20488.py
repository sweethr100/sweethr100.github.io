import random
import os
import sys

def printMap(data):
    os.system("cls")
    for y in data:
        for x in y:
            sys.stdout.write("\033[42m")
            if x == 0:
                sys.stdout.write("\033[32m")
                print("0",end=" ")
                sys.stdout.write("\033[30m")
            else:
                print(x,end=" ")
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

def left(data):
    for z in range(len(data)-1):
        for y in range(len(data)):
            for x in range(len(data[y])-1):
                if data[y][x] == 0:
                        data[y][x] = data[y][x+1]
                        data[y][x+1] = 0
    return data

def sumdata(data):
    for y in range(len(data)):
        for x in range(len(data[y])-1):
            if data[y][x] == data[y][x+1]:
                data[y][x]*=2
                data[y][x+1] = 0
    return data

def move(data,user):
    if user == "a":
        data = left(data)
        data = sumdata(data)
        data = left(data)
    elif user == "d":
        data = rotation(rotation(data))
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(rotation(data))
    elif user == "s":
        data = rotation(rotation(rotation(data)))
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(data)
    elif user == "w":
        data = rotation(data)
        data = left(data)
        data = sumdata(data)
        data = left(data)
        data = rotation(rotation(rotation(data)))

    return data

def push(data):
    tmp = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                tmp.append([y,x])
    if len(tmp) > 0:
        r = random.choice([2,2,2,2,4])
        y,x = random.choice(tmp)
        data[y][x]=r
    return data

if __name__ == "__main__":
    data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    while True:
        data = push(data)
        printMap(data)
        user = input()
        data = move(data,user)