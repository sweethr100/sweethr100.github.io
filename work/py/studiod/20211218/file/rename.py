import os

user = input("File Name : ")
file = open(user+".txt","r",encoding="utf-8")
data = file.read()
file.close()
user2 = input("New Name : ")
file = open(user2+".txt","w",encoding="utf-8")
file.write(data)
file.close()
os.unlink(user+".txt")