def dfs(graph, visited, now, colored, color):
    visited[now] = True
    if colored[now] not in (0, color):
        return "NO"
    colored[now] = color
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, colored, 3 - color)
    return "YES"

f = open("input.txt")
lines = f.read().splitlines()
f.close()

n, m = map(int, lines[0].split())

graph = [[] for _ in range(0, n+1)]
visited = [False]*(n+1)
colored = [0] * (n+1)
for i in range(1, m+1):
    v1, v2 = map(int, lines[i].split())
    if v1 != v2:
        graph[v1].append(v2)
        graph[v2].append(v1)

print(dfs(graph, visited, 1, colored, 1))
