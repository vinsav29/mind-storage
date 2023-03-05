def solution(n, k):
    if k == 1:
        return 1
    s = [1, 1]
    step = 1
    for i in range(2, n):
        step = step * 2
        if i > k:
            step -= s[i-k-1]
        s.append(step)


    return step


n, k = map(int, input().split())
print(solution(n, k))