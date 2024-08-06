def check(data):
    for i in range(2,data):
        if data%i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(30):
        print(i,check(i))