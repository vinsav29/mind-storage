def solution(n, words):
    checkSet = set()
    resultSet = set()
    for w in words:
        prevC = ""
        cnt = 1
        newW = ""

        for i, c in enumerate(w):
            if c == prevC:
                cnt += 1
                if cnt == 3:
                    cnt = 2
                    continue
            else:
                cnt = 1
            newW += c
            prevC = c
        if newW not in checkSet:
            resultSet.add(newW)
        else:
            resultSet.remove(newW)

    return len(resultSet)

t = int(input())
for _ in range(t):
    n = int(input())
    words = []
    for _ in range(n):
        words.append(str(input()))
    print(solution(n, words))
