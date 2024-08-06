pb = []


def add():
    # 추가
    name = input("이름 : ")
    phone = input("전화번호 : ")
    email = input("이메일 : ")
    birth = input("생일 : ")
    p = {'name': name, 'phone': phone, 'email': email, 'birth': birth}
    pb.append(p)


def delete():
    name = input("이름: ")
    i = 0
    while i < len(pb):
        if pb[i]['name'] == name:
            del pb[i]


def update():
    delete()
    add()


def view():
    for p in pb:
        print(p)


if __name__ == "__main__":
    add()
    add()
    add()
