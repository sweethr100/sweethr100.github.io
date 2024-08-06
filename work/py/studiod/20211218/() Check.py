
def check(data):
    gal = []
    for i in data:
        if i == "(":
            gal.append("(")
        elif i == ")":
            if not gal == []:
                gal.pop(0)
            else:
                return False
    if not gal == []:
        return False

    return True

if __name__ == "__main__":
    print(check("()()"))
    print(check("(())"))
    print(check(")("))
    print(check("(()"))
    print(check("())"))
    while True:
        print(check(input("체크 : ")))
