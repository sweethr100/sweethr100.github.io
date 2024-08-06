import sys

pb = []

def add():
	# 추가
	name = input("이름 : ")
	phone = input("전화번호 : ")
	email = input("이메일 : ")
	birth = input("생일 : ")
	p = {'name':name,'phone':phone,'email':email,'birth':birth}
	pb.append(p)
def view():
	for p in pb:
		print(p)

def delete(name):
	i=0
	while i<len(pb):
		if pb[i]['name'] == name:
			del pb[i]
		else:
			i+=1

def update(name):
	for i in range(len(pb)):
		if pb[i]['name'] == name:
			pb[i]['phone'] = input("전화번호 : ")
			pb[i]['email'] = input("이메일 : ")
			pb[i]['birth'] = input("생일 : ")

def menu():
	print("전화번호부")
	print("1. 추가")
	print("2. 확인")
	print("3. 삭제")
	print("4. 수정")
	print("5. 종료")
	return int(input(">: "))

if __name__ == "__main__":
	while True:
		a = menu()
		if a== 1:
			add()
		elif a== 2:
			view()
		elif a== 3:
			delete(input("이름 : "))
		elif a== 4:
			update(input("이름 : "))
		elif a ==5:
			break