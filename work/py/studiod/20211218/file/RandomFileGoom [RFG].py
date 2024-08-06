import random
fp = open("eng.txt","r",encoding="utf-8")
line = fp.readlines()
key = random.choice(line)
key = key.strip()
print(key)
fp.close()
