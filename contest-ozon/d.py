from collections import Counter


def solution(n, t):
    c = Counter(t)
    places = dict()
    place = 1
    prevKey = -1
    for key in sorted(c):
        if key - prevKey == 1:
            places[key] = places[prevKey]
        else:
            places[key] = place
        place += c[key]
        prevKey = key
    results = ""
    for guy in t:
        results += str(places[guy]) + " "
    return results

t = int(input())
for t in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(solution(n, s))
