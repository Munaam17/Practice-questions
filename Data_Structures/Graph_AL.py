# Adding a node in undirectional graph
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []

# Adding an edge in undirectional graph with cost
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        # list1 = (v2, cost)
        # list2 = (v1, cost)
        graph[v1].append(v2)
        graph[v2].append(v1)

# Adding an edge in directional graph with cost
# def add_edge_d(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "is not present in graph")
#     elif v2 not in graph:
#         print(v2, "is not present in graph")
#     else:
#         list1 = (v2, cost)
#         graph[v1].append(list1)

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

def DFS(node, visited, graph):
    if node not in graph:
        print(node,"is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)

def DFSiterative(node, graph):
    visited = set()
    if node not in graph:
        print("node is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


# BFS

def BFS(graph, visited, node):
    if node not in graph:
        print("Node not present in graph")
        return
    Queue = []
    Queue.append(node)
    visited.add(node)
    while Queue:
        current = Queue.pop(0)
        print(current)
        for i in graph[current]:
            if i not in visited:
                Queue.append(i)
                visited.add(i)



graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("F")
add_edge("A", "B", 50)
add_edge("F", "C", 40)
add_edge("D", "F", 30)
add_edge("D", "B", 20)
add_edge("A", "F", 30)
add_edge("D", "B", 20)
# add_edge_d("D", "F", 30)
# add_edge_d("A", "D", 20)
# add_edge_d("C", "A", 30)
DFS("A", set(), graph)
print()
DFSiterative("A", graph)
print()
BFS(graph, set(), "C")
# del_node("F")
# # del_node("C")
# del_nod_w("B")
# del_nod_w("A")
print(graph)

