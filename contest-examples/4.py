def solution(rows, cols, table, clicks):
    sortedSet = set()
    indicies = [*range(rows)]
    for c in clicks:
        column_id = c - 1
        if column_id not in sortedSet:
            indicies.sort(key=lambda idx: table[idx][column_id])

    for row_id in indicies:
        print(" ".join([str(row) for row in table[row_id]]))
    print()


t = int(input())
for i in range(t):
    input()
    n, m = map(int, input().split())
    table = []
    for row in range(n):
        table.append(list(map(int, input().split())))

    k = int(input())
    clicks = list(map(int, input().split()))

    solution(n, m, table, clicks)

# 1
# 4 3
# 3 4 1
# 2 2 5
# 2 4 2
# 2 2 1
# 3
# 2 1 3