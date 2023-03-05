def solution(n, prices):
    count = {}
    total = 0
    for p in prices:
        count[p] = count.get(p, 0) + 1
        if count[p] % 3 == 0:
            pass    # third item for free
        else:
            total += p
    print(total)


t = int(input())

for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    solution(n, p)
