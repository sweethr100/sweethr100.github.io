def solution(data):
    tmp = []
    for i in data:
        if i != 0:
            tmp.append(i)
        elif i == 0:
            if len(tmp) > 0:
                tmp.pop()

    return sum(tmp)

if __name__ == "__main__":fs
    data = [1,2,0,0,5]
    print(solution(data))
    data = [0,1,0,3,7]
    print(solution(data))
    data = [5,7,9,8]
    print(solution(data))
    data = [1,0,0,4]
    print(solution(data))