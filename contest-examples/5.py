def solution(n, a):
    hashDone = set()
    for i in range(1, n):
        if a[i] in hashDone:
            return "NO"
        if a[i] != a[i-1]:
            hashDone.add(a[i-1])
    return "YES"


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solution(n, a))

