import random

def random_word(fname):
    file = open(fname,"r",encoding="utf8")
    keywords = file.readlines()
    file.close()
    keyword = random.choice(keywords)
    return keyword.rstrip()

def update(answer,view,user):
    view = list(view)
    for i in range(len(answer)):
        if answer[i] == user:
            view[i] = user
    return "".join(view)

def isEnd(view):
    if "_" in view:
        return False

    return True

if __name__ == "__main__":
    answer = random_word("dict.txt")
    view = "_"*len(answer)

    while True:
        tmp = list(view)
        tmp = " ".join(tmp)
        print(tmp)
        user = input(">: ")[0]
        view = update(answer,view,user)
        if isEnd(view) == True:
            print(answer)
            print("End")
            break