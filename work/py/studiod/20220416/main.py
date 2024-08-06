from posixpath import split


def function(data):
    
    length = len(data)**0.5
    if length % 1 != 0:
        length=int(length)+1

    result = []
    cnt = 0
    for y in range(int(length)):
        tmp = []
        for x in range(int(length)):
            if cnt < len(data):
                tmp.append(data[cnt])
            else:
                tmp.append(None)
            cnt+=1

        result.append(tmp)

    return result

if __name__ == "__main__":
    print(function([]))
    print(function([1]))
    print(function([1,2]))
    print(function([1,2,3]))
    print(function([1,2,3,4,5,6,7]))
    print()