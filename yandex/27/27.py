

f = open("input.txt")
lines = f.read().splitlines()
f.close()

n, m = map(int, lines[0].split())
a = [[(-1, "S")]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    j = 1
    for v in map(int, lines[i].split()):
        if i == j == 1:
            a[i][j] = (v, "S")
        else:
            left, top = a[i][j-1], a[i-1][j]
            if left > top:
                a[i][j] = (left[0] + v, "R")
            else:
                a[i][j] = (top[0] + v, "D")
        j += 1

trace = []
i, j = n, m
while a[i][j][1] != "S":
    x = a[i][j][1]
    trace.append(x)
    if x == "D":
        i -= 1
    if x == "R":
        j -= 1
print(a[-1][-1][0])
print(" ".join(reversed(trace)))