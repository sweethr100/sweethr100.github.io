user = input("복사할 파일 이름 : ")

infile = open(user,"r",encoding="utf8")
data = infile.read()
infile.close()

user = input("복사한 새 파일 이름 : ")
outfile = open(user,"w",encoding="utf8")
outfile.write(data)
outfile.close()