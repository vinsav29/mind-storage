


f = open("input.txt")
lines = f.read().splitlines()
f.close()

total = int(lines[0])
arr = list(map(int, lines[1].split()))
s = sorted(arr)
res = [1000]*total
res[1] = s[1]-s[0]
for i in range(2,total):
    di = s[i]-s[i-1]
    res[i] = min(res[i-1]+di, res[i-2]+di)

print(res[-1])
