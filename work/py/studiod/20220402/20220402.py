# class Parent():
#     def __init__(self):
#         print("부모 생성")
#     def __del__(self):
#         print("부모 소멸")
#
#     # def print(self):
#     #     print("부모")
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("자식 생성")
#     def __del__(self):
#         print("자식 소멸")
#         super().__del__()
#
#     def print(self):
#         print("자식")
#
#
# if __name__ == "__main__":
#     # c = Child()
#     # c.print()
#
#     p = Parent()
#     p.print()





# from turtle import *
#
# click = 0
#
# class MyTurtle(Turtle):
#     def glow(self,x,y):
#         global click
#         self.fillcolor("red")
#         self.shape("turtle")
#         click+=1
#         print(click)
#         # self.size(click)
#
# turtle = MyTurtle()
# turtle.onclick(turtle.glow)
#
# mainloop()





import module

module.hello()
module.bye()