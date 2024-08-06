import random

def solution(data):
    for i in range(len(data)):
        data[i] = str(data[i])
    data.sort()
    data = "".join(data)
    return int(data)

    return data

if __name__ == "__main__":
    data = []

    for i in range(5):
        data.append(random.randint(1,99))

    print(data)
    print(solution(data))