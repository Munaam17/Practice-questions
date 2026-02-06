from collections import deque
import heapq    

# Adding a node in undirectional graph
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []

# Adding an edge in undirectional graph with cost
# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "is not present in graph")
#     elif v2 not in graph:
#         print(v2, "is not present in graph")
#     else:
#         list1 = (v2, cost)
#         list2 = (v1, cost)
#         graph[v1].append(v2)
#         graph[v2].append(v1)

# Adding an edge in directional graph with cost
def add_edge_d(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        list1 = (v2, cost)
        graph[v1].append(list1)

# deleting the node from undirected & directed graph

def del_node(v):
    if v not in graph:
        print(v, "is not present in graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

# deleting the node from undirected & directed weighted graph

def del_nod_w(v):
    if v not in graph:
        print(v, "is not present in graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j [0]:
                    list1.remove(j)
                    break

# DFS

# def DFS(node, visited, graph):
#     if node not in graph:
#         print(node,"is not present in graph")
#         return
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i, visited, graph)

# def DFSiterative(node, graph):
#     visited = set()
#     if node not in graph:
#         print("node is not present in the graph")
#         return
#     stack = []
#     stack.append(node)
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             print(current)
#             visited.add(current)
#             for i in graph[current]:
#                 stack.append(i)


# BFS

def BFS(graph, visited1, node):
    if node not in graph:
        print("Node not present in graph")
        return
    Queue = []
    Queue.append(node)
    visited1.add(node)
    while Queue:
        current = Queue.pop(0)
        print(current)
        for i in graph[current]:
            if i not in visited1:
                Queue.append(i)
                visited1.add(i)

def Shortest_path(node, target, graph):
    if node not in graph:
        print(node,"not present in graph")
    elif target not in graph:
        print(target,"not present in graph")
    else:
        visited2 ={}
        queue = deque()
        visited2[node] = None
        queue.append(node)
        while queue:
            current = queue.popleft()
            if current == target:
                path = []
                while current is not None:
                    path.append(current)
                    current = visited2[current]
                return path[::-1]
            for i in graph[current]:
                if i not in visited2:
                    visited2[i] = current
                    queue.append(i)
        return None


graph = {}
visited1 = set()
# add_node("A")
# add_node("B")
# add_node("C")
# add_node("D")
# add_node("F")
# add_node("E")
# add_edge("A", "B", 50)
# add_edge("F", "C", 40)
# add_edge("D", "F", 30)
# add_edge("D", "B", 20)
# add_edge("A", "F", 30)
# add_edge("D", "B", 20)

# Addition of node and edge
add_node("A")
add_node("a")
add_node("B")
add_node("C")
add_node("D")
add_node("F")
add_node("E")
add_node("G")
add_edge_d("A", "B", 1)
add_edge_d("F", "C", 3)
add_edge_d("B", "F", 5)
add_edge_d("G", "E", 6)
add_edge_d("C", "B", 3)
add_edge_d("E", "A", 6)
add_edge_d("D", "E", 7)
# add_edge("E")
# add_edge_d("D", "F", 30)
# add_edge_d("A", "D", 20)
# add_edge_d("C", "A", 30)
# DFS("A", set(), graph)
# print()
# DFSiterative("A", graph)


# BFS(graph, visited1, "A")
print()
# BFS(graph, visited1, "E")
print()
# print(Shortest_path("A","G", graph))
# print(Shortest_path("A","C", graph))
# # del_node("F")
# # del_node("C")
# del_nod_w("B")
# del_nod_w("A")
print(graph)

# For checking if the graph is connected or disconnected
for i in list(graph):
    if i not in visited1:
        print("Given graph is a disconnected graph")
        break
else:
    print("Graph is not disconnect, it's connected")

print(list(graph))

# Dijkstra's Algorithm

def Dijkstra(graph, start):
    if start not in graph:
        print(start,"not present in graph!")
        return
    distance = {item:float("inf") for item in graph}
    distance [start] = 0
    queue = [(0, start)]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_dist > distance[curr_node]:
            continue
        # for node, weight in graph [curr_node]:
        for node, weight in graph [curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distance [node]:
                distance[node] = new_dist
                heapq.heappush(queue,(new_dist,node))

    return distance

print(Dijkstra(graph, "A"))

# que = []
# heapq.heappush(que, (3, 9))
# heapq.heappush(que, (1, 6))
# heapq.heappush(que, (2, 3))

# print(heapq.heappop(que))
# print(heapq.heappop(que))
# print(heapq.heappop(que))
