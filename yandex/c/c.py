import heapq


def main():
    f = open("input.txt")
    lines = f.read().splitlines()
    f.close()

    n = int(lines[0])
    st = []
    ans = [None] * n
    for i in range(n):
        a, b = map(int, lines[i+1].split())
        heapq.heappush(st, (-(a + b), i))
    first, second = 0, 0
    while st:
        time, pos = heapq.heappop(st)
        if first <= second:
            first += -time
            ans[pos] = 1
        else:
            second += -time
            ans[pos] = 2
    print(" ".join(str(k) for k in ans))


main()