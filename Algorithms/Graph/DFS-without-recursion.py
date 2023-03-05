import sys

def dfs(graph, visited, now, comp, comp_list):
    visited[now] = True
    comp_list[comp].append(str(now))
    non_visited = set()
    for neig in graph[now]:
        if not visited[neig]:
            # dfs(graph, visited, neig, comp)
            non_visited.add(neig)
    return non_visited

f = open("DFS-without-recursion.txt")
lines = f.read().splitlines()
f.close()

n, m = map(int, lines[0].split())

# sys.setrecursionlimit(n)
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(1, m+1):
    v1, v2 = map(int, lines[i].split())
    if v1 != v2:
        graph[v1].append(v2)
        graph[v2].append(v1)

comp = 0
comp_list = []
for i, v in enumerate(graph):
    if i == 0:
        continue
    if not visited[i]:
        comp_list.append([])
        non_visited = set()
        non_visited.update(dfs(graph, visited, i, comp, comp_list))
        while len(non_visited) > 0:
            non_visited.update(dfs(graph, visited, non_visited.pop(), comp, comp_list))
        comp += 1


print(len(comp_list))
for c in comp_list:
    print(len(c))
    print(" ".join(c))
