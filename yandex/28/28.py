n, m = map(int, input().split())
a = [[0]*(m+1) for _ in range(n+1)]
maxD = (n + m - 2) // 3

x = y = 1
a[x][y] = 1
d = 0   # starting diagonale
while d < maxD:
    for i in range(x, y-1, -1):
        for j in range(y, x+1, 1):
            if i + 2 <= n and j + 1 <= m:
                a[i+2][j+1] += a[i][j]
            if i + 1 <= n and j + 2 <= m:
                a[i + 1][j + 2] += a[i][j]
    x, y = x + 2, y + 1
    d += 1
print(a[n][m])