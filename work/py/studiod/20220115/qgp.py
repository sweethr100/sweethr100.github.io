file = open("dict.txt","r")
dict = file.readlines()
dict.sort()
for line in dict:
    print(line,end="")

file.close()