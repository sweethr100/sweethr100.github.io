def solution(data):
    cnt = 0
    for i in range(10):
        if i not in data:
            cnt+=i
    return cnt

if __name__ == '__main__':

    data =[1,2,3,4,5,6,7,8,0]
    print(solution(data))

    data =[1,2,3,4,6,7,8,0]
    print(solution(data))

    data =[5,8,4,0,6,7,9]
    print(solution(data))