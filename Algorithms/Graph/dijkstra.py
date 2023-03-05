# def Dijkstra(N, S, matrix):
# 	valid = [True]*N
# 	weight = [1000000]*N
# 	weight[S] = 0
# 	for i in range(N):
# 		min_weight = 1000001
# 		ID_min_weight = -1
# 		for j in range(N):
# 			if valid[j] and weight[j] < min_weight:
# 				min_weight = weight[j]
# 				ID_min_weight = j
# 		for z in range(N):
# 			if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
# 				weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
# 		valid[ID_min_weight] = False
# 	return weight

graph = dict()
graph["start"] = dict(a=6, b=2)
graph["a"] = dict(fin=1)
graph["b"] = dict(a=3, fin=5)
graph["fin"] = dict()

infinity = float("inf")
costs = dict(a=6, b=2, fin=infinity)

parents = dict(a="start", b="start", fin=None)

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# Алгори́тм Де́йкстры (англ. Dijkstra’s algorithm) — алгоритм на графах для нахождения кратчайшего
# расстояния от одной из вершин графа до всех остальных. Алгоритм работает только для графов без рёбер
# отрицательного веса.


# Задача №1
#
# Будем называть узким местом пути в графе ребро максимальной длины в этом пути.
# Путём с минимальным узким местом назовём такой путь между вершинами s и t,
# что не существует другого пути s \rightarrow t, чьё узкое место меньше по длине.
# Требуется построить алгоритм, который вычисляет путь с минимальным узким местом
# для двух данных вершин в графе. Асимптотическая сложность такого алгоритма должна быть O(m\log{n})

graph = dict()
graph["start"] = dict(a=5, b=2)
graph["a"] = dict(fin=1)
graph["b"] = dict(a=3, fin=5)
graph["fin"] = dict()

infinity = float("inf")
costs = dict(a=5, b=2, fin=infinity)

parents = dict(a="start", b="start", fin=None)

processed = []

