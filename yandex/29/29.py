f = open("input.txt")
lines = f.read().splitlines()
f.close()

n = int(lines[0])
cost = list(map(int, lines[1:n+1]))
cost.insert(0, 300)

a = [[(300*n, 0)]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):     # day
    for j in range(0, n+1): #coupone
        dp = [(300*n, 0)]

        # first day, cant use coupones
        if i == 1:
            if cost[i] > 100:
                a[i][1] = (cost[i], 0)
            else:
                a[i][0] = (cost[i], 0)
            break

        # waste coupone
        if j < n:
            # dp.append(a[i-1][j+1])
            dp.append((a[i - 1][j + 1][0], 1))

        # waste money
        if cost[i] > 100 and j > 0:
            dp.append((a[i-1][j-1][0] + cost[i], -1))
        if cost[i] <= 100:
            dp.append((a[i-1][j][0] + cost[i], 0))

        a[i][j] = min(dp)

minA = (300*n, 0)
maxId = -1
for idx, val in enumerate(a[n]):
    if val[0] < minA[0]:
        minA = val
        maxId = idx
    if val == minA:
        maxId = idx
print(minA[0])

res = []
i = n
j = maxId
used = 0
days = []
while i > 0:
    dj = a[i][j][1]
    if dj == 1:
        used += 1
        days.append(str(i))

    i, j = i-1, j+dj


print(maxId, used)
print(" ".join(reversed(days)))