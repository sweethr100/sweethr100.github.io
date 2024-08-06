import random

data = []

key = [
    [],[],[],[],[],[],[],[],[],[]
]

for i in range(30):
    data.append(random.randint(0,9999))

print(data)

step=1
for z in range(len(str(max(data)))):
    for i in range(len(data)):
        s=-1
        if step == 1:
            s = data[i]%10
        else:
            s = (data[i]//step)%10
        key[s].append(data[i])

    data=[]
    print(z,"회 key: ",key)
    for y in range(len(key)):
        while 0<len(key[y]):
            data.append(key[y].pop(0))
    step*=10
    print(z,"회 data: ",data)
    print("---------------------------------------")
    print(data)