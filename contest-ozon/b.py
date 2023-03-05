from collections import defaultdict


def solution(s):
    stat = {1: 4, 2: 3, 3: 2, 4: 1}
    items = defaultdict(int)
    for a in s:
        items[a] += 1
    for item in items:
        if stat[item] != items[item]:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    s = list(map(int, input().split()))
    print(solution(s))


