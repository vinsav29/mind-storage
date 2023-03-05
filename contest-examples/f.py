def parse_timestamp(dt):
    h, m, s = map(int, dt.split(":"))
    if not 0 <= h <= 23 or not 0 <= m <= 59 or not 0 <= s <= 59:
        raise ValueError
    return h*3600 + m*60 + s


def solution(n, intervals):
    intervalList = []
    for interval in intervals:
        start, stop = interval.split("-")
        try:
            start, stop = parse_timestamp(start), parse_timestamp(stop)
        except ValueError:
            return "NO"
        if stop - start < 0:
            return "NO"
        intervalList.append([start, stop])

    sortedVals = sorted(intervalList, key=lambda item: item[0])
    for i in range(n-1):
        if sortedVals[i][1] >= sortedVals[i+1][0]:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = int(input())
    intervals = []
    for _ in range(n):
        intervals.append(input())

    print(solution(n, intervals))

