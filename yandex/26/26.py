


f = open("input.txt")
lines = f.read().splitlines()
f.close()

n, m = map(int, lines[0].split())
a = [[100 * 40]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    j = 1
    for v in map(int, lines[i].split()):
        if i == j == 1:
            a[i][j] = v
        else:
            a[i][j] = min(a[i][j-1], a[i-1][j]) + v
        j += 1
print(a[-1][-1])