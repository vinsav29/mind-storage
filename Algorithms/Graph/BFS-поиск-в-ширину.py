from collections import deque


graph = {}
graph["you"] = [ "alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = [ ]

def person_is_seller(name):
    return name == "peggy"

# сложность - О(количество ребер).
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")

# adj = [
# #список смежности
#     [1,3], # 0
#     [0,3,4,5], # 1
#     [4,5], # 2
#     [0,1,5], # 3
#     [1,2], # 4
#     [1,2,3] # 5
# ]
#
# level = [-1] * len(adj)
# print(level)
# #список уровней вершин
#
# def bfs(s):
#     global level
#     level[s] = 0
# # уровень начальной вершины
#     queue = [s]
#  # добавляем начальную вершину в очередь
#     while queue:
#  # пока там что-то есть
#         v = queue.pop(0)
#  # извлекаем вершину
#         for w in adj[v]:
# # запускаем обход из вершины v
#             if level[w] == -1:
# # проверка на посещенность
#                 queue.append(w)
# # добавление вершины в очередь
#                 level[w] = level[v] + 1
# # подсчитываем уровень вершины
#
# for i in range(len(adj)):
#     if level[i] == -1:
#         bfs(i)
#  # на случай, если имеется несколько компонент связности
#
# print(level)
# # уровень вершины 2
