f = open("input.txt")
lines = f.read().splitlines()
f.close()

n = int(lines[0])
aN = list(map(int, lines[1].split()))
m = int(lines[2])
aM = list(map(int, lines[3].split()))

s = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        maxS = max(s[i-1][j], s[i][j-1], s[i-1][j-1])
        s[i][j] = maxS
        if maxS == s[i-1][j-1] and aN[i-1] == aM[j-1]:  # 0 to N-1, M-1
            s[i][j] += 1

i, j = n, m
res = []
maxS = s[i][j]
while maxS > 0:
    # maxS = max(s[i-1][j], s[i][j-1], s[i-1][j-1])

    # check aN == aM?
    if aN[i - 1] == aM[j - 1]:
        res.append(str(aN[i - 1]))
        maxS -= 1
        # if maxS == 0:
        #     print(maxS)

    # newI, newJ, newMaxS = i, j, maxS
    for di, dj in zip((-1, -1, 0), (-1, 0, -1)):
        x, y = i + di, j + dj

        if s[x][y] == maxS:     # same val, cont seeking
            i, j = x, y
            break
# for i in range(1000-10,1000+1):
#     print(s[i][1000-10:1000+1])

print(" ".join(reversed(res)))
