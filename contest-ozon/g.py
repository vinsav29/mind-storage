from collections import defaultdict


def dfs(w, i, dir):
    # can we slide element i?
    return {i: dir}

def solution(n, m, windows):
    hashW = dict()
    doubles = dict()
    for i, w in enumerate(windows):
        if w in hashW:
            doubles[w] = i
        else:
            hashW[w] = i

    slides = dict()

    def backtrack(doubles, hashW):
        # check

        backtrack(doubles, hashW)

    backtrack(doubles, windows)
    return


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    w = list(input().split())
    print(solution(n, m, w))