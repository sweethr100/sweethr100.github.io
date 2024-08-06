import random

user = int(input(">: "))
data = []
flag = True

while len(data) < user:
    r = (random.randint(1,100))
    if flag and r%2==1:
        data.append(r)
        flag=False

    elif not flag and r%2==0:
        data.append(r)
        flag=True

solo=[]
double=[]

for i in data:
    if i%2==1:
        solo.append(i)
    elif i%2==0:
        double.append(i)

solo.sort(reverse=False)
double.sort(reverse=True)

flag=True
re=[]
for i in range(len(solo)):
    re.append(solo[i])
    if len(double) > i:
        re.append(double[i])

print(re)
# print(solo)
# print(double)