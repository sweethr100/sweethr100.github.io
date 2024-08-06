class Parent():
    def __init__(self):
        print("부모 생성")
    def __del__(self):
        print("부모 소멸")

class Child(Parent):
    def __init__(self):
        print("자식 생성")
    def __del__(self):
        print("자식 소멸")

if __name__ == "__main__":
    p=Child()