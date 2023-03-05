def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

f = open("input.txt")
lines = f.read().splitlines()
f.close()

n, m = map(int, lines[0].split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(1, m+1):
    v1, v2 = map(int, lines[i].split())
    if v1 != v2:
        graph[v1].append(v2)
        graph[v2].append(v1)
dfs(graph, visited, 1)
# print(graph)
# print(visited)

res = []
s = 0
for i in range (1, n+1):
    if visited[i]:
        s += 1
        res.append(str(i))
print(s)
print(" ".join(res))