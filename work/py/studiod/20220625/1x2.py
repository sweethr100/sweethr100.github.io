from audioop import mul


def solution(data):
    score = 0
    multiple = 0
    for i in range(len(data)):
        if data[i] == "O":
            score+=1+multiple
            multiple+=1
        if data[i] == "X":
            multiple=0
    
    return score

if __name__ == "__main__":
    print(solution("OXOOOXXOXOX"))
    print(solution("OXOXOXO"))
    print(solution("XXOOXX"))