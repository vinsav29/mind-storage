


f = open("input.txt")
lines = f.read().splitlines()
f.close()

n = int(lines[0])

virtual_guy = (float("inf"),)*3

guys = [
    virtual_guy,
    virtual_guy,
    virtual_guy,
]
a, b, c = 0, 1 ,2
dp = [0, 0, 0]
# total = 0
i = 3 #current
for line in lines[1:]:
    guys.append(tuple(map(int, line.split())))
    dp.append(0)

    dp[i] = min(dp[i-1] + guys[i][a], dp[i-2] + guys[i-1][b], dp[i-3] + guys[i-2][c])

    # total += dp[i]

    guys.pop(0)
    dp.pop(0)
print(dp[2])
