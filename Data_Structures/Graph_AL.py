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
        list1 = (v2, cost)
        list2 = (v1, cost)
        graph[v1].append(list1)
        graph[v2].append(list2)

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
add_edge_d("D", "F", 30)
add_edge_d("A", "D", 20)
add_edge_d("C", "A", 30)
del_node("F")
# del_node("C")
del_nod_w("B")
print(graph)

