import random
import copy

blockcolor = {
    0 : (238, 228, 218),
    2 : (238,228,218),
    4 : (237,224,200),
    8 : (242,177,121),
    16 : (245,149,99),
    32 : (246,124,95),
    64 : (246,94,59),
    128 : (237,207,114),
    256 : (237,204,97),
    512 : (237,200,80),
    1024 : (237,197,63),
    2048 : (237,194,46)
}

class Game2048():

    def __init__(self,level=2048):

        # 방향 설정
        self.LEFT = 'a'
        self.RIGHT = 'd'
        self.UP = 'w'
        self.DOWN = 's'

        #  게임 변수 설정
        self.map = [] #논리 맵
        self.size = 4 # 맵 가로세로 크기
        self.level = level # 현재 설정 레벨
        self.score = 0 # 점수

        # 맵 생성
        # 4*4 리스트 생성 및 0으로 초기화
        for i in range(self.size):
            self.map.append([0]*self.size)

        # 블럭 랜덤 추가
        self.blockAdd()
        self.blockAdd()

    #블럭 추가 함수
    def blockAdd(self):
        #블럭 확률 정의 (2 : 75% , 4 25%)
        t = [2,2,2,4]

        while True:
            # 맵에 0이 존재하지 않는다면 종료
            if(not self.isZero()):
                break
            r = t[random.randint(0, len(t) - 1)]
            y = random.randint(0, 3)
            x = random.randint(0, 3)

            # 맵에 0이 존재하면 블럭추가
            if self.map[y][x] == 0:
                self.map[y][x] = r
                break

    # 맵에 0이 포함되었는 확인
    def isZero(self):
        cnt=0
        for i in self.map:
            if i.count(0) != 0:
                cnt+=1
        if cnt == 0:
            return False
        else:
            return True

    # 맵 출력 (CONSOLE 모드 테스트)
    def print(self):
        print("score : ",self.score)
        for y in self.map:
            for x in y:
                print("%4d"%x,end=" ")
            print("")
        print('------------------------------')

    # 맵 왼쪽으로 90도 회전
    def lotate(self):
        buf = copy.deepcopy(self.map)
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map[x][self.size-1-y] = buf[y][x]

    # 블럭 왼쪽으로 밀기
    def leftPush(self):
        for z in range(self.size):
            for y in range(self.size):
                for x in range(self.size-1):
                    if self.map[y][x] == 0:
                        self.map[y][x]=self.map[y][x+1]
                        self.map[y][x+1]=0

    #현재 블럭과 오른쪽 블럭이 같을 경우 합치기
    def merge(self):
        for y in range(self.size):
            for x in range(self.size-1):
                if self.map[y][x] == self.map[y][x+1]:
                    self.score = self.score+self.map[y][x]
                    self.map[y][x] *= 2
                    self.map[y][x + 1] = 0

    # 게임 성공 여부
    # 맵 안에 설정된 레벨의 숫자가 있으면 True
    def isSuccess(self):
        for y in self.map:
            for x in y:
                if x == self.level:
                    return True
        return False

    # 게임 실패 여부
    # 움직일 수 없는 경우 True
    def isFail(self):
        for y in range(self.size):
            for x in range(self.size-1):
                if self.map[y][x] == self.map[y][x+1]:
                    return False
        for y in range(self.size-1):
            for x in range(self.size):
                if self.map[y][x] == self.map[y+1][x]:
                    return False
        return True


# 콘솔 모드 테스트
if __name__ == "__main__":
    game = Game2048()
    while True:
        # 블럭 추가
        game.blockAdd()
        game.blockAdd()
        #화면 출력
        game.print()
        #성공여부
        if (game.isSuccess()):
            break
        #실패 여부
        if (game.isFail()):
            break
        # 사용자 입력
        key = input("key")[0]

        # 블럭 이동
        # 맵을 회전시켜 4방향 동작
        if key == game.LEFT:
            pass
        elif key == game.DOWN:
            game.lotate()
        elif key == game.RIGHT:
            game.lotate()
            game.lotate()
        elif key == game.UP:
            game.lotate()
            game.lotate()
            game.lotate()

        game.leftPush()
        game.merge()
        game.leftPush()

        if key == game.LEFT:
            pass
        elif key == game.DOWN:
            game.lotate()
            game.lotate()
            game.lotate()
        elif key == game.RIGHT:
            game.lotate()
            game.lotate()
        elif key == game.UP:
            game.lotate()

