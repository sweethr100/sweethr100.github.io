# from turtle import *
# alex = Turtle()
#
# alex.forward(100)
# alex.left(90)
# alex.forward(200)
#
# mainloop()





# class Car:
#     def drive(self):
#         self.speed = 60
#
# myCar = Car()
# myCar.speed = 0
# myCar.model = "E-Class"
# myCar.color = "blue"
# myCar.year = "2017"
#
# print("자동차 객체를 생성하였습니다.")
# print("자동차의 속도는", myCar.speed)
# print("자동차의 색상은", myCar.color)
#
# print("자동차의 모델은", myCar.model)
# print("자동차를 주행합니다.")
# myCar.drive()
# print("자동차의 속도는", myCar.speed)





# class Car:
#     def __init__(self,speed,color,model):
#         self.speed = speed
#         self.color = color
#         self.model = model
#
#     def drive(self):
#         self.speed = 60
#
# myCar = Car(0,"blue","E-Class")
#
# print("자동차 객체를 생성하였습니다.")
# print("자동차의 속도는", myCar.speed)
# print("자동차의 색상은", myCar.color)
# print("자동차의 모델은", myCar.model)
# print("자동차를 주행합니다")
# myCar.drive()
# print("자동차의 속도는", myCar.speed)





# import time
#
# class Car:
#     def __init__(self):
#         print("생성자")
#
#     def __del__(self):
#         print("소멸자")
#
# car = Car()
# del car
# time.sleep(10)
# print("메러ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ엉")





# class Car:
#     def __init__(self,speed,color,model):
#         self.speed = speed
#         self.color = color
#         self.model = model
#
#     def __str__(self):
#         msg = "속도:"+str(self.speed)+" 색상:"+self.color+" 모델:"+self.model
#         return msg
#
#     def drive(self):
#         self.speed = 60
#
# dadCar = Car(0,"silver","A6")
# momCar = Car(0,"white","520d")
# myCar = Car(0,"blue","E-Class")
#
# print(dadCar)
# print(momCar)
# print(myCar)





# from turtle import *
#
# t1 = Turtle()
# t1.shape("circle")
#
# t2 = Turtle()
# t2.shape("turtle")
#
# t3 = Turtle()
# t3.shape("square")
#
# t1.penup()
# t2.penup()
# t1.goto(0,100)
# t2.goto(0,50)
# t1.pendown()
# t2.pendown()
#
# while True:
#     t1.circle(100)
#     t2.circle(150)
#     t3.circle(200)





from turtle import *
class Car:
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape("car.gif")
myCar = Car(400, "red", "E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()