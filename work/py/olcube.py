import random

def createMap(cnt=3):
    data = []
    i=1
    for y in range(cnt):
        tmp=[]
        for x in range(cnt):
            tmp.append(i)
            i+=1
        data.append(tmp)
    return data

def showMap(data=[],cnt=3):
    for j in data:
        for i in j:
            if i != cnt*cnt:
                print("%4d"%i,end="")
            else:
                print("    ",end="")
        print("")

def userinput():
    user = input("입력 : ")
    return user

def getXY(data,cnt):
    for y in range(cnt):
        for x in range(cnt):
            if data[y][x] == cnt*cnt:
                 return x, y

def move(data, cnt, x, y, tx, ty):
    if ty < 0 or ty >= cnt or tx < 0 or tx >= cnt:
        return

    data[y][x],data[ty][tx] = data[ty][tx], data[y][x]

def movement(data,level,x,y,user):
    if user == "w":
        move(data, level, x, y, x, y - 1)
    elif user == "s":
        move(data, level, x, y, x, y + 1)
    elif user == "a":
        move(data, level, x, y, x - 1, y)
    elif user == "d":
        move(data, level, x, y, x + 1, y)

def mix(data,level):
    flags = ['w','a','s','d']
    for i in range(1000):
        r = random.choice(flags)
        x,y = getXY(data, level)
        movement(data, level, x, y, r)
    return data

if __name__ == "__main__":
    level= 2
    data = createMap(level)
    data = mix(data,level)

    while True:
        showMap(data,level)
        x, y = getXY(data, level)
        user = userinput()
        movement(data,level,x,y,user)